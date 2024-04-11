from django import template

from cosmetics_store.orders.models import OrderModel

register = template.Library()


@register.filter
def count_products(user):
    order_qs = OrderModel.objects.filter(user=user, is_ordered=False)
    if order_qs.exists():
        total_quantity = sum([order_product.quantity for order_product in order_qs.first().products.all()])
        return total_quantity

    return ""


