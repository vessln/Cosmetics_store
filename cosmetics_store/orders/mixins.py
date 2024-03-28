from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect


class MyCartRestrictionMixin(auth_mixins.LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs["pk"] or not request.user.is_superuser:
            return redirect("home page")

        return super().dispatch(request, *args, **kwargs)