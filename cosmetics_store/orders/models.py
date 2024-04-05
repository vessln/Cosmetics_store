from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from cosmetics_store.orders.helpers import generate_unique_number
from cosmetics_store.products.models import ProductModel

UserModel = get_user_model()


class UserShippingAddressModel(models.Model):
    MAX_COUNTRY_LENGTH = 30
    MAX_CITY_LENGTH = 50
    MAX_STREET_LENGTH = 30
    MAX_NOTES_LENGTH = 100

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    country = models.CharField(
        max_length=MAX_COUNTRY_LENGTH,
        null=False,
        blank=False,
    )

    city = models.CharField(
        max_length=MAX_CITY_LENGTH,
        null=False,
        blank=False,
    )

    street_address = models.CharField(
        max_length=MAX_STREET_LENGTH,
        null=False,
        blank=False,
    )

    notes = models.TextField(
        max_length=MAX_NOTES_LENGTH,
        null=True,
        blank=True,
    )


class OrderProductModel(models.Model):  # acts like a link between products and order
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MaxValueValidator(10),]
    )

    is_ordered = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"Product: {self.product.title_product}, count: {self.quantity}"

    def get_product_sum(self):
        return self.quantity * self.product.price


class OrderModel(models.Model):  # this order store all the products that user was added in shopping card
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    shipping_address = models.ForeignKey(
        UserShippingAddressModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    products = models.ManyToManyField(
        OrderProductModel,
    )

    start_date = models.DateTimeField(
        auto_now_add=True,
    )

    completion_order_date = models.DateField(
        null=True,
        blank=True,
    )

    is_ordered = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    order_id = models.IntegerField(
        default=generate_unique_number(),
        null=True,
        blank=True,
    )

    total_sum = models.FloatField(
        default=0.0,
    )

