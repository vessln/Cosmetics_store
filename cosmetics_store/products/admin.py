from django.contrib import admin

from cosmetics_store.products.models import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    pass
