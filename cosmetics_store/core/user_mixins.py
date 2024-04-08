from django.contrib import messages
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect


class RestrictedUserAccessMixin(auth_mixins.LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user.pk != kwargs["pk"]:
            messages.info(request, "You have not access to this page!")
            return redirect("home page")

        return super().dispatch(request, *args, **kwargs)


class LogoutRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in to the site!")
            return redirect("details user", pk=request.user.pk)

        return super().dispatch(request, *args, **kwargs)


class PageRestrictionMixin(auth_mixins.LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        return redirect("home page")


class RestrictedStaffUsers(auth_mixins.LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if ((request.user.is_authenticated and not request.user.is_staff) or
                (request.user.is_authenticated and request.user.is_superuser)):
            return super().dispatch(request, *args, **kwargs)

        else:
            messages.info(request, "You have no permission to access this page!")  # 403
            return redirect("home page")

