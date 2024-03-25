from django.urls import path

from cosmetics_store.orders.views import add_product_to_cart, remove_product_from_cart, MyCartView, \
    decrease_product_quantity_in_cart

urlpatterns = (
    path("<slug:slug>/add-to-cart/", add_product_to_cart, name="add to cart"),
    path("<slug:slug>/remove-from-cart/", remove_product_from_cart, name="remove from cart"),
    path("<slug:slug>/decrease_product_quantity/", decrease_product_quantity_in_cart, name="decrease product quantity"),
    path("my-cart/", MyCartView.as_view(), name="my cart"),

)