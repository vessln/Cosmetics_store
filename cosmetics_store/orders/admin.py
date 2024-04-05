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
    list_display = ("product", "quantity", "is_ordered", "user")
    fields = ("quantity", )
    list_filter = ("product", "quantity", "user")
    ordering = ("user",)
    search_fields = ("product", "quantity", "user")


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "shipping_address", "completion_order_date", "is_ordered", "order_id", "total_sum")
    fields = ("order_id", "total_sum")
    list_filter = ("user", "is_ordered", "total_sum")
    ordering = ("completion_order_date", )
    search_fields = ("user", "completion_order_date", "is_ordered")
