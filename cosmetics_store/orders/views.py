from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.views import generic as generic_views

from cosmetics_store.orders.models import OrderProductModel, OrderModel
from cosmetics_store.products.models import ProductModel


@login_required
def add_product_to_cart(request, slug):
    product = get_object_or_404(ProductModel, slug=slug)
    order_product, created = OrderProductModel.objects.get_or_create(
        product=product,
        user=request.user,
        is_ordered=False
    )

    uncompleted_order_qs = OrderModel.objects.filter(user=request.user, is_ordered=False)

    if uncompleted_order_qs.exists():  # make with try / except ?
        uncompleted_order = uncompleted_order_qs[0]  # .first() ?
        if uncompleted_order.products.filter(product__slug=product.slug).exists():
            order_product.quantity += 1
            order_product.save()
            messages.info(request, f"{product.title_product} +1")
        else:
            uncompleted_order.products.add(order_product)
            messages.info(request, "The product was added to your cart!")
            return redirect("details product", slug=slug)

    else:
        new_order = OrderModel.objects.create(user=request.user, start_date=timezone.now())
        new_order.products.add(order_product)
        messages.info(request, "The product was added to your cart!")

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
        uncompleted_order = uncompleted_order_qs[0]
        # if the ordered product is in the order:
        if uncompleted_order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProductModel.objects.filter(
                product=product,
                user=request.user,
                is_ordered=False
            )[0]
            order_product.delete()
            messages.info(request, "The product was removed from your cart!")
        else:
            messages.info(request, "This product is not in your cart.")
            return redirect("details product", slug=slug)

    else:
        messages.info(request, "You dont have current order.")
        return redirect("details product", slug=slug)

    return redirect("details product", slug=slug)


class MyCartView(generic_views.ListView):
    model = OrderModel
    template_name = "orders/my_cart.html"

    def get_queryset(self):
        # Retrieve orders for the current user
        return OrderModel.objects.filter(user=self.request.user, is_ordered=False)

