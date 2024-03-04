from django.urls import path

from cosmetics_store.blog.views import blog_view, article_view

urlpatterns = (
    path("all_articles/", blog_view, name="blog all articles"),
    path("article/", article_view, name="article"),
)