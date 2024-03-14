from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from cosmetics_store.blog.forms import CreateArticleForm, UpdateArticleForm
from cosmetics_store.blog.models import ArticleModel


class CreateArticleView(generic_views.CreateView):
    model = ArticleModel
    form_class = CreateArticleForm
    template_name = "blog/create_article.html"

    success_url = reverse_lazy("details article")


class UpdateArticleView(generic_views.UpdateView):
    model = ArticleModel
    form_class = UpdateArticleForm
    template_name = "blog/create_article.html"

    success_url = reverse_lazy("edit article")


class DetailsArticleView(generic_views.DetailView):
    model = ArticleModel
    template_name = "blog/details_article.html"


class DeleteArticleView(generic_views.DeleteView):
    model = ArticleModel
    template_name = "blog/delete_article.html"
    success_url = reverse_lazy("list articles")


class ListArticlesView(generic_views.ListView):
    queryset = ArticleModel.objects.order_by("-published_at")
    template_name = "blog/list_articles.html"
    # paginate_by = 3

    @property
    def searched_word(self):
        return self.request.GET.get("searched_word", None)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["searched_word"] = self.searched_word or ""

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.searched_word
        if search:
            queryset = ArticleModel.objects.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )

        return queryset

    # def get(self, request, *args, **kwargs):
    #     if self.searched_word:
    #         queryset = self.get_queryset()
    #
    #         if queryset.exists():
    #             pk_article = self.queryset.first().pk
    #
    #             return redirect(request.META.get("HTTP_REFERER") + f"#article-{pk_article}")
    #
    #     return super().get(request, *args, **kwargs)



