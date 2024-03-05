from django.shortcuts import render
from django.views import generic as generic_views

from cosmetics_store.blog.models import Article


class CreateArticleView(generic_views.CreateView):
    pass


class EditArticleView(generic_views.UpdateView):
    pass


class DetailsArticleView(generic_views.DetailView):
    queryset = Article.objects.all()
    template_name = "blog/details_article.html"


class DeleteArticleView(generic_views.DeleteView):
    pass


class ListArticlesView(generic_views.ListView):
    queryset = Article.objects.order_by("-published_at")
    template_name = "blog/list_articles.html"
