from django.shortcuts import render
from django.views import generic as generic_views

from cosmetics_store.blog.models import ArticleModel
from cosmetics_store.orders.models import OrderModel
from cosmetics_store.products.models import ProductModel

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class HomePageView(generic_views.TemplateView):
    template_name = "common/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["best_sellers"] = ProductModel.objects.order_by("-sales_count")[:3]
        context["latest_articles"] = ArticleModel.objects.order_by("-published_at")[:3]
        context["unprocessed_orders_count"] = OrderModel.objects.filter(is_sent=False).count()

        return context


def about(request):
    total_users = UserModel.objects.count()
    total_orders = OrderModel.objects.count()
    total_products = ProductModel.objects.count()

    context = {
        "total_users": total_users,
        "total_orders": total_orders,
        "total_products": total_products,
    }

    return render(request, "common/about.html", context)

