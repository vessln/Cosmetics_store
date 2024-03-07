from django.urls import path, include

from cosmetics_store.blog.views import ListArticlesView, CreateArticleView, EditArticleView, DetailsArticleView, \
    DeleteArticleView


urlpatterns = (
    path("articles/", ListArticlesView.as_view(), name="list articles"),
    path("article/create/", CreateArticleView.as_view(), name="create article"),
    path("article/<int:pk>/",
         include([
             path("edit/", EditArticleView.as_view(), name="edit article"),
             path("details/", DetailsArticleView.as_view(), name="details article"),
             path("delete/", DeleteArticleView.as_view(), name="delete article"),
             ]),
         ),

)