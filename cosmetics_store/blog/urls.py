from django.urls import path

from cosmetics_store.blog.views import blog_view

urlpatterns = (
    path("all_articles/", blog_view, name="blog all articles"),
)