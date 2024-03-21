from django.urls import path

from cosmetics_store.orders.views import add_product_to_cart

urlpatterns = (
    path("<slug:slug>/add-to-cart/", add_product_to_cart, name="add to cart"),

)