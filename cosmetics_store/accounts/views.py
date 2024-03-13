from django.contrib.auth import views as auth_views, get_user_model, login, logout
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect
from django.views import generic as generic_views
from django.urls import reverse_lazy

from cosmetics_store.accounts.forms import LoginUserForm, RegisterUserForm

UserModel = get_user_model()


class RegisterUserView(generic_views.CreateView):
    template_name = "accounts/register_user.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("home page")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)  # log the user in after registration

        return result


class LoginUserView(auth_views.LoginView):
    template_name = "accounts/login_user.html"
    form_class = LoginUserForm
    success_url = reverse_lazy("home page")


def logout_user(request):
    logout(request)
    return redirect("home page")


class DetailsUserView(auth_mixins.LoginRequiredMixin, generic_views.DetailView):
    model = UserModel
    template_name = "accounts/details_user.html"


class UpdateUserView(generic_views.UpdateView):
    model = UserModel
    template_name = "accounts/edit_user.html"
    success_url = reverse_lazy("details user")


class DeleteUserView(generic_views.DeleteView):
    model = UserModel
    template_name = "accounts/delete_user.html"
    success_url = reverse_lazy("home page")
