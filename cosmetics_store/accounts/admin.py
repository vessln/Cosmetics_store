from django.contrib import admin

from cosmetics_store.accounts.models import StoreUserModel


@admin.register(StoreUserModel)
class StoreUserModelAdmin(admin.ModelAdmin):
    pass

