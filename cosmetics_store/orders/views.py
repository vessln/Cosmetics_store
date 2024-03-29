from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.db.models import F

from django.views import generic as generic_views, View

from cosmetics_store.accounts.forms import UserShippingAddressForm
from cosmetics_store.orders.models import OrderProductModel, OrderModel
from cosmetics_store.products.models import ProductModel


# if order is empty -> remove it:
def remove_empty_order(current_order):
    if current_order.products.count() < 1:
        current_order.delete()


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
            order_product.delete()
            messages.info(request, "The product was removed from your cart.")
            remove_empty_order(uncompleted_order)
            return redirect("my cart")
        # else:
        #     messages.info(request, "This product is not in your cart.")
        #     return redirect("details product", slug=slug)

    return redirect("my cart")


@login_required
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


class MyCartView(auth_mixins.LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            current_order = OrderModel.objects.get(user=self.request.user, is_ordered=False)
            current_order.total_sum = sum([order_product.get_product_sum() for order_product in current_order.products.all()])
            current_order.save()
            context = {"object": current_order}
            return render(self.request, "orders/my_cart.html", context)

        except ObjectDoesNotExist:
            return render(self.request, "orders/my_cart.html")

    # def form_valid(self, form):
    #     # Get the product slug from the form or any other source
    #     product_slug = form.cleaned_data["product_slug"]
    #
    #     # Retrieve the product object based on the slug
    #     product = get_object_or_404(ProductModel, slug=product_slug)
    #
    #     # Retrieve the OrderProductModel instance based on the current user and product
    #     order_product, created = OrderProductModel.objects.get_or_create(
    #         user=self.request.user,
    #         product=product,
    #         defaults={'quantity': 0}  # Set a default value for quantity if the instance is newly created
    #     )
    #accounts_storeusermodel_user_permissions
    #     # Update the quantity of the OrderProductModel instance
    #     order_product.quantity += form.cleaned_data["quantity"]
    #
    #     # Save the updated OrderProductModel instance
    #     order_product.save()


class CheckoutView(auth_mixins.LoginRequiredMixin, generic_views.FormView):
    form_class = UserShippingAddressForm
    template_name = "orders/checkout.html"

    def get_success_url(self):
        return reverse("thank you")

    def form_valid(self, form):
        # set current user who create the order to `user` in UserShippingAddressModel
        form.instance.user = self.request.user
        shipping_address = form.save()

        current_order = OrderModel.objects.filter(user=self.request.user, is_ordered=False).first()
        if current_order:
            current_order.shipping_address = shipping_address
            current_order.is_ordered = True

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


# TODO: make custom mixin: users who haven't active orders cannot access checkout page!


class SuccessfulOrder(auth_mixins.LoginRequiredMixin, generic_views.TemplateView):
    template_name = "orders/thank_you.html"

    #TODO: Send an email

