from django.urls import path

from cosmetics_store.common.views import home_page, about

urlpatterns = (
    path("", home_page, name="home page"),
    path("about/", about, name="about"),

)