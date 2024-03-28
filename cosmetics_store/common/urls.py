from django.urls import path

from cosmetics_store.common.views import HomePageView, about

urlpatterns = (
    path("", HomePageView.as_view(), name="home page"),
    path("about/", about, name="about"),

)