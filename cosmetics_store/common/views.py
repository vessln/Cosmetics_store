from django.shortcuts import render
from django.views import generic as generic_views

from cosmetics_store.blog.models import ArticleModel
from cosmetics_store.products.models import ProductModel

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class HomePageView(generic_views.TemplateView):
    template_name = "common/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_products"] = ProductModel.objects.order_by("-created_at")[:3]
        context["latest_articles"] = ArticleModel.objects.order_by("-published_at")[:3]
        # context["total_orders"] =
        context["users"] = UserModel.objects.count()

        return context


def about(request):
    return render(request, "common/about.html")

