from django import template

register = template.Library()


@register.filter
def join_product_quantity(order):
    details = []
    for ordered_product in order.products.all():
        title = ordered_product.product.title_product
        quantity = ordered_product.quantity
        details.append(f"{title} x {quantity}")

    return "; ".join(details)