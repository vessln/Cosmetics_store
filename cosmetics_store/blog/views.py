from django.contrib.messages import views as messages_views
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as generic_views

from cosmetics_store.blog.forms import CreateArticleForm, UpdateArticleForm
from cosmetics_store.blog.models import ArticleModel


class CreateArticleView(generic_views.CreateView):
    model = ArticleModel
    form_class = CreateArticleForm
    template_name = "blog/create_article.html"

    def form_valid(self, form):  # set currently authenticated user who create the article to `author`
        form = super().form_valid(form)
        self.object.author = self.request.user
        self.object.save()
        return form

    def get_success_url(self):
        return reverse("details article", kwargs={"pk": self.object.pk})


class UpdateArticleView(generic_views.UpdateView):
    model = ArticleModel
    form_class = UpdateArticleForm
    template_name = "blog/edit_article.html"

    def get_success_url(self):
        return reverse("details article", kwargs={"pk": self.object.pk})


class DetailsArticleView(generic_views.DetailView):
    model = ArticleModel
    template_name = "blog/details_article.html"


class DeleteArticleView(messages_views.SuccessMessageMixin, generic_views.DeleteView):
    model = ArticleModel
    success_message = "The article was successfully deleted!"
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







