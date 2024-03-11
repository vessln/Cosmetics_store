from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    password2 = forms.CharField(
        label="Confirm Password",
        help_text="",
    )

    class Meta:
        model = UserModel
        fields = ("email", "username", "date_of_birth", "phone", "password1", "password2",)

        labels = {
            "email": "Your email",
            "date_of_birth": "Birth date",
            "phone": "Phone number",
            }

        widgets = {
            "date_of_birth": forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"}),
            "phone": forms.TextInput(attrs={"placeholder": "0*********"}),
        }

        help_texts = {
            "username": "",
            "password2": "",
        }


class LoginUserForm(auth_forms.AuthenticationForm):
    widgets = {
        "username": forms.TextInput(attrs={"placeholder": "Username"}),
        "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
    }
