from django import forms

from cosmetics_store.core.mixins import FormControlFieldsMixin
from cosmetics_store.orders.models import UserShippingAddressModel, OrderModel


class UserShippingAddressForm(FormControlFieldsMixin, forms.ModelForm):
    fields_requiring_form_control = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._make_fields_form_control()

    class Meta:
        model = UserShippingAddressModel
        fields = ("country", "city", "street_address", "notes", )

        widgets = {
            "country": forms.TextInput(attrs={"placeholder": "Country", }),
            "city": forms.TextInput(attrs={"placeholder": "City", }),
            "street_address": forms.TextInput(attrs={"placeholder": "Street, №", }),
            "notes": forms.Textarea(attrs={"placeholder": "Write your notes...", "rows": 3, }),
        }


class SentOrderForm(forms.ModelForm):
    fields_requiring_form_control = "__all__"

    class Meta:
        model = OrderModel
        fields = ("is_sent",)
        widgets = {
           "is_sent": forms.RadioSelect(choices=((True, "Yes"), (False, "No"))),
        }
