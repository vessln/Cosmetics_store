from django.contrib import messages
from django.contrib.auth import views as auth_views, get_user_model, login, logout
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.contrib.messages import views as messages_views
from django.shortcuts import redirect
from django.views import generic as generic_views
from django.urls import reverse_lazy, reverse

from cosmetics_store.accounts.forms import LoginUserForm, RegisterUserForm, UpdateUserForm
from cosmetics_store.core.user_mixins import RestrictedUserAccessMixin, LogoutRequiredMixin
from cosmetics_store.orders.models import OrderModel

UserModel = get_user_model()


class RegisterUserView(LogoutRequiredMixin, generic_views.CreateView):
    template_name = "accounts/register_user.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("home page")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)  # log the user in after registration

        return result


class LoginUserView(LogoutRequiredMixin, auth_views.LoginView):
    template_name = "accounts/login_user.html"
    form_class = LoginUserForm
    success_url = reverse_lazy("home page")


@login_required
def logout_user(request):
    logout(request)
    messages.info(request, "You were successfully logged out.")
    return redirect("home page")


class DetailsUserView(RestrictedUserAccessMixin, generic_views.DetailView):
    model = UserModel
    template_name = "accounts/details_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_successful_orders"] = OrderModel.objects.filter(user=self.request.user, is_ordered=True).count()

        return context


class UpdateUserView(RestrictedUserAccessMixin, messages_views.SuccessMessageMixin, generic_views.UpdateView):
    model = UserModel
    form_class = UpdateUserForm
    success_message = "The profile was successfully edited!"
    template_name = "accounts/edit_user.html"

    def get_success_url(self):
        return reverse("details user", kwargs={"pk": self.object.pk})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = self.form_class(instance=self.object)
    #     context["form"] = form
    #
    #     return context


class DeleteUserView(RestrictedUserAccessMixin, messages_views.SuccessMessageMixin, generic_views.DeleteView):
    model = UserModel
    success_message = "The profile was successfully deleted!"
    template_name = "accounts/delete_user.html"
    success_url = reverse_lazy("home page")
