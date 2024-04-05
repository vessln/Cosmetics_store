from django.contrib import admin

from cosmetics_store.accounts.models import StoreUserModel


@admin.register(StoreUserModel)
class StoreUserModelAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "phone", "gender",
                    "date_of_birth", "is_staff", "is_superuser")
    fields = ("first_name", "last_name", "phone", "gender", "date_of_birth", "is_staff", "is_superuser", "groups")
    list_filter = ("username", "gender", "is_staff", "is_superuser")
    ordering = ("username", "first_name")
    search_fields = ("username", "first_name", "last_name", "phone", "is_staff", "is_superuser")



