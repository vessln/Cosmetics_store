from django.contrib import messages
from django.shortcuts import redirect


class RestrictedUserAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user.pk != kwargs["pk"]:
            messages.info(request, "You have not access to this page!")
            return redirect("home page")

        return super().dispatch(request, *args, **kwargs)


class RegistrationAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You have already a registration!")
            return redirect("home page")

        return super().dispatch(request, *args, **kwargs)





