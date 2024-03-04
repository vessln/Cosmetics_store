from django.db import models


class OrderProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        )

    quantity = models.PositiveIntegerField(
        default=1,
    )


class Order(models.Model):
    user = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
    )

    products_to_buy = models.ManyToManyField(
        OrderProduct,
    )

    start_date = models.DateTimeField(
        auto_now_add=True,
    )
