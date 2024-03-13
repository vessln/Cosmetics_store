from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

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
