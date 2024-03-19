from django.contrib import admin

from cosmetics_store.orders.models import OrderProductModel, OrderModel


@admin.register(OrderProductModel)
class OrderProductAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    pass
