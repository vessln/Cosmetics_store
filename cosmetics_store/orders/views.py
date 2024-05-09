from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.db.models import F

from django.views import generic as generic_views, View

from cosmetics_store.core.decorator import restricted_staff_users
from cosmetics_store.core.user_mixins import PageRestrictionMixin, RestrictedStaffUsers
from cosmetics_store.orders.forms import UserShippingAddressForm, SentOrderForm
from cosmetics_store.orders.helpers import generate_unique_number
from cosmetics_store.orders.models import OrderProductModel, OrderModel
from cosmetics_store.products.models import ProductModel


UserModel = get_user_model()


# if order is empty -> remove it:
def remove_empty_order(current_order):
    if current_order.products.count() < 1:
        current_order.delete()


@restricted_staff_users
@login_required
def add_product_to_cart(request, slug):
    product = get_object_or_404(ProductModel, slug=slug)
    order_product, created = OrderProductModel.objects.get_or_create(
        product=product,
        user=request.user,
        is_ordered=False,
    )

    uncompleted_order_qs = OrderModel.objects.filter(user=request.user, is_ordered=False)

    if uncompleted_order_qs.exists():
        uncompleted_order = uncompleted_order_qs.first()
        if uncompleted_order.products.filter(product__slug=product.slug).exists():
            if order_product.quantity >= 10:
                messages.info(request, "You have reached the maximum amount of this product.")
            else:
                order_product.quantity += 1
                order_product.save()

            if request.path.endswith("/add-to-cart/"):
                messages.info(request, f"{order_product.product.title_product} was added to your cart.")
                return redirect(request.META.get("HTTP_REFERER"))

        else:
            uncompleted_order.products.add(order_product)
            return redirect("details product", slug=slug)

    else:
        new_order = OrderModel.objects.create(user=request.user, start_date=timezone.now())
        new_order.products.add(order_product)

    messages.info(request, f"{order_product.product.title_product} was added to your cart.")

    return redirect("details product", slug=slug)


@restricted_staff_users
@login_required
def remove_product_from_cart(request, slug):
    # get a product:
    product = get_object_or_404(ProductModel, slug=slug)
    # check if user has an order:
    uncompleted_order_qs = OrderModel.objects.filter(user=request.user, is_ordered=False)

    # if user have an order:
    if uncompleted_order_qs.exists():
        # get the order:
        uncompleted_order = uncompleted_order_qs.first()
        # if the ordered product is in the order:
        if uncompleted_order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProductModel.objects.filter(
                product=product,
                user=request.user,
                is_ordered=False
            ).first()
            uncompleted_order.products.remove(order_product)
            order_product.delete()
            messages.info(request, "The product was removed from your cart.")
            remove_empty_order(uncompleted_order)
            return redirect("my cart")
        # else:
        #     messages.info(request, "This product is not in your cart.")
        #     return redirect("details product", slug=slug)

    return redirect("my cart")


@login_required
@restricted_staff_users
def decrease_product_quantity_in_cart(request, slug):
    product = get_object_or_404(ProductModel, slug=slug)
    uncompleted_order_qs = OrderModel.objects.filter(user=request.user, is_ordered=False)

    if uncompleted_order_qs.exists():
        uncompleted_order = uncompleted_order_qs.first()
        if uncompleted_order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProductModel.objects.filter(
                product=product,
                user=request.user,
                is_ordered=False,
            ).first()

            if order_product.quantity > 1:
                order_product.quantity -= 1
                order_product.save()
                messages.info(request, f"The quantity of '{order_product.product.title_product}' was decreased.")
            else:
                order_product.delete()
                messages.info(request, "The product was removed from your cart.")

                remove_empty_order(uncompleted_order)

            return redirect("my cart")


class MyCartView(RestrictedStaffUsers, View):
    def get(self, *args, **kwargs):
        try:
            current_order = OrderModel.objects.get(user=self.request.user, is_ordered=False)
            current_order.total_sum = sum([order_product.get_product_sum() for order_product in current_order.products.all()])
            current_order.save()
            context = {"object": current_order}
            return render(self.request, "orders/my_cart.html", context)

        except ObjectDoesNotExist:
            return render(self.request, "orders/my_cart.html")


class CheckoutView(RestrictedStaffUsers, generic_views.FormView):
    form_class = UserShippingAddressForm
    template_name = "orders/checkout.html"

    def get_success_url(self):
        return reverse("thank you")

    def form_valid(self, form):
        if not self.request.user.first_name or not self.request.user.last_name or not self.request.user.phone:
            messages.info(
                self.request,
                "To complete your order you need to provide your first name, last name and phone number.")

            return redirect("edit user", pk=self.request.user.pk)

        # set current user who create the order to `user` in UserShippingAddressModel
        form.instance.user = self.request.user
        shipping_address = form.save()

        current_order = OrderModel.objects.filter(user=self.request.user, is_ordered=False).first()
        if current_order:
            current_order.shipping_address = shipping_address
            current_order.completion_order_date = timezone.now().date()
            current_order.order_id = (f"{self.request.user.username[:2]}"
                                      f"{generate_unique_number()}"
                                      f"{self.request.user.pk}")
            current_order.is_ordered = True

            current_orderproduct = OrderProductModel.objects.filter(user=self.request.user, is_ordered=False).first()
            current_orderproduct.is_ordered = True
            current_orderproduct.save()

            for order_product in current_order.products.all():
                order_product.product.sales_count = F("sales_count") + order_product.quantity
                order_product.product.save()

            current_order.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get products and their quantity, which are in uncompleted user's order:
        current_order = OrderModel.objects.filter(user=self.request.user, is_ordered=False
                                                  ).prefetch_related("products__product").first()

        if current_order:
            context["current_order"] = current_order

        return context


class SuccessfulOrder(auth_mixins.LoginRequiredMixin, generic_views.TemplateView):
    template_name = "orders/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["placed_order"] = OrderModel.objects.filter(user=self.request.user, is_ordered=True).last()

        return context


class CurrentProcessingOrders(PageRestrictionMixin, generic_views.FormView):
    template_name = "orders/order_processing.html"
    form_class = SentOrderForm

    def get_success_url(self):
        return reverse("home page")

    def get_order(self):
        orders = OrderModel.objects.filter(is_ordered=True, is_sent=False).order_by("-completion_order_date")
        if orders.exists():
            return orders.first()
        return None

    def form_valid(self, form):
        order = self.get_order()
        if order:
            order.is_sent = form.cleaned_data["is_sent"]
            order.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["first_placed_order"] = self.get_order

        return context





