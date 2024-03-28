from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect


class OrderRestrictionMixin(auth_mixins.LoginRequiredMixin,):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff or not request.user.is_superuser:
            return redirect("home page")

        return super().dispatch(request, *args, **kwargs)