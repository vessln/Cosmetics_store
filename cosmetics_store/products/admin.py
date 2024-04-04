from django.contrib import admin

from cosmetics_store.products.models import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title_product", "category", "brand", "price", "description", "ingredients",
                    "image_product", "created_at", "sales_count", "slug", "manager")
    list_filter = ("category", "brand", "manager")
    ordering = ("price", "sales_count", )
    search_fields = ("title_product", "category", "brand", "manager")
    fieldsets = (
        ("Product", {"fields": ("category", "price"), }),
        ("Product details", {"fields": ("description", "ingredients", ), })
    )
