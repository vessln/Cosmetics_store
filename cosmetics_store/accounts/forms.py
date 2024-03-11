from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email", "username", "date_of_birth", "phone", "password1", "password2",)

    labels = {
        "email": "Your email",
        "date_of_birth": "Birth date",
        "password1": "Password",
        "password2": "Confirm password",
        }

    widgets = {
        "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        "username": forms.TextInput(attrs={"placeholder": "Username"}),
        "date_of_birth": forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"}),
        "password1": forms.PasswordInput(attrs={"placeholder": "Password"}),
        "password2": forms.PasswordInput(attrs={"placeholder": "Confirm password"}),
    }


class LoginUserForm(auth_forms.AuthenticationForm):
    widgets = {
        "username": forms.TextInput(attrs={"placeholder": "Username"}),
        "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
    }
