from django import template

from cosmetics_store.orders.models import OrderModel

register = template.Library()


@register.filter
def count_products(user):
    if user.is_authenticated:
        order_qs = OrderModel.objects.filter(user=user, is_ordered=False)
        if order_qs.exists():
            return order_qs[0].products.count()

    return 0

