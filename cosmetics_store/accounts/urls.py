from django.urls import path, include

from cosmetics_store.accounts.views import RegisterUserView, LoginUserView, DetailsUserView, UpdateUserView, \
    DeleteUserView, logout_user

urlpatterns = (
    path("register/", RegisterUserView.as_view(), name="register user"),
    path("login/", LoginUserView.as_view(), name="login user"),
    path("logout/", logout_user, name="logout user"),
    path("<int:pk>/",
         include([
             path("details/", DetailsUserView.as_view(), name="details user"),
             path("edit/", UpdateUserView.as_view(), name="edit user"),
             path("delete/", DeleteUserView.as_view(), name="delete user"),
                ]),
         ),
    )