from django import template

register = template.Library()


@register.filter
def filter_products():
    pass
