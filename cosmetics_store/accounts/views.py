from django.contrib.auth import views as auth_views, get_user_model, login, logout
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect
from django.views import generic as generic_views
from django.urls import reverse_lazy, reverse

from cosmetics_store.accounts.forms import LoginUserForm, RegisterUserForm, UpdateUserForm

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

# TODO - make success url logic !!!


def logout_user(request):
    logout(request)
    return redirect("home page")


class DetailsUserView(auth_mixins.LoginRequiredMixin, generic_views.DetailView):
    model = UserModel
    template_name = "accounts/details_user.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["orders_count"] = self.UserModel.orders.count()
    #
    #     return context


class UpdateUserView(generic_views.UpdateView):
    model = UserModel
    form_class = UpdateUserForm
    template_name = "accounts/edit_user.html"

    def get_success_url(self):
        return reverse("details user", kwargs={"pk": self.object.pk})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = self.form_class(instance=self.object)
    #     context["form"] = form
    #
    #     return context


class DeleteUserView(generic_views.DeleteView):
    model = UserModel
    template_name = "accounts/delete_user.html"
    success_url = reverse_lazy("home page")
