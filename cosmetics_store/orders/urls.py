from django.urls import path

from cosmetics_store.orders.views import add_product_to_cart, remove_product_from_cart, \
    decrease_product_quantity_in_cart, MyCartView, CheckoutView, SuccessfulOrder

urlpatterns = (
    path("<slug:slug>/add-to-cart/", add_product_to_cart, name="add to cart"),
    path("<slug:slug>/remove-from-cart/", remove_product_from_cart, name="remove from cart"),
    path("<slug:slug>/decrease_product_quantity/", decrease_product_quantity_in_cart, name="decrease product quantity"),
    path("my-cart/", MyCartView.as_view(), name="my cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("thank-you/", SuccessfulOrder.as_view(), name="thank you"),

)