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

    else:
        new_order = OrderModel.objects.create(user=request.user, start_date=timezone.now())
        new_order.products.add(order_product)
        messages.info(request, "The product was added to your cart!")

    return redirect("details product", kwargs={slug: slug})


