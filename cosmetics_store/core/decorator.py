from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


def restricted_staff_users(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if ((request.user.is_authenticated and not request.user.is_staff) or
                (request.user.is_authenticated and request.user.is_superuser)):
            return view_func(request, *args, **kwargs)

        else:
            messages.info(request, "You have no permission to access this page!")  # 403
            return redirect(reverse_lazy("home page"))

    return _wrapped_view
