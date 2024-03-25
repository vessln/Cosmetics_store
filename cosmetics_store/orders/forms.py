from django import forms
from django.contrib.auth import get_user_model

from cosmetics_store.orders.models import OrderProductModel

UserModel = get_user_model()


class ProductQuantityForm(forms.ModelForm):
    class Meta:
        model = OrderProductModel
        fields = ["quantity"]

