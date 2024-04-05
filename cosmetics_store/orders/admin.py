from django.contrib import admin

from cosmetics_store.orders.models import OrderProductModel, OrderModel, UserShippingAddressModel


@admin.register(UserShippingAddressModel)
class UserShippingAddressModelAdmin(admin.ModelAdmin):
    list_display = ("country", "city", "street_address", "user")
    fields = ("country", "city", "street_address")
    list_filter = ("country", "city", "user")
    ordering = ("country", "city")
    search_fields = ("country", "city", "user")


@admin.register(OrderProductModel)
class OrderProductAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    pass
