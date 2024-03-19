from django.contrib.auth import get_user_model
from django.db import models

from cosmetics_store.products.models import ProductModel

UserModel = get_user_model()


class OrderProductModel(models.Model):  # to link the order and products with current order
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
    )

    # order = models.ForeignKey(
    #     Order,
    #     on_delete=models.CASCADE,
    #     )

    quantity = models.PositiveIntegerField(
        default=1,
    )


class OrderModel(models.Model):  # this order store all the products that user was added in shopping card
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    products_to_buy = models.ManyToManyField(
        OrderProductModel,
    )

    start_date = models.DateTimeField(
        auto_now_add=True,
    )

    is_ordered = models.BooleanField(
        default=False,
    )
