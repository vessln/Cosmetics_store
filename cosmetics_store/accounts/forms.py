from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from cosmetics_store.accounts.models import UserShippingAddressModel

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm password"

    class Meta:
        model = UserModel
        fields = ("username", "email", "date_of_birth", "gender", "phone", "password1", "password2",)

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email address"}),
            "date_of_birth": forms.DateInput(attrs={"placeholder": "Birth date: YYYY-MM-DD"}),
            "phone": forms.TextInput(attrs={"placeholder": "0*********"}),
            "gender": forms.RadioSelect(choices=UserModel.GENDER_CHOICES, attrs={"class": "form-control"}),
        }

        error_messages = {
            "email": {
                "invalid": "Please, enter a valid email address in the format `john@email.com`",
            },
            "date_of_birth": {
                "invalid": "Please, enter a valid date in the format `YYYY-MM-DD`.",
            },
            "gender": {
                "required": "Please, select your gender. This field is required.",
            },
        }


class LoginUserForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["password"].widget.attrs["placeholder"] = "Password"


class UpdateUserForm(auth_forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["readonly"] = "readonly"
        self.fields["email"].widget.attrs["readonly"] = "readonly"
        self.fields["date_of_birth"].widget.attrs["readonly"] = "readonly"

    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = ("username", "email", "date_of_birth", "first_name", "last_name", "phone",)

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter your first name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter your last name"}),
        }


class UserShippingAddressForm(forms.ModelForm):
    class Meta:
        model = UserShippingAddressModel
        fields = ("country", "city", "street_address", "notes", )

        widgets = {
            "country": forms.TextInput(attrs={"placeholder": "Country", "class": "form-control", }),
            "city": forms.TextInput(attrs={"placeholder": "City", "class": "form-control", }),
            "street_address": forms.TextInput(attrs={"placeholder": "Street, №", "class": "form-control",}),
            "notes": forms.TextInput(attrs={"placeholder": "Write your notes...", "class": "form-control",}),
        }


