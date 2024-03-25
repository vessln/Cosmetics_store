from django.contrib.auth import get_user_model
from django.db import models

from cosmetics_store.accounts.models import CheckoutShippingAddressModel
from cosmetics_store.products.models import ProductModel

UserModel = get_user_model()


class OrderProductModel(models.Model):  # acts like a link between products and order
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    is_ordered = models.BooleanField(
        default=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
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
        CheckoutShippingAddressModel,
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

    is_ordered = models.BooleanField(
        default=False,
    )

    def get_total_sum(self):
        total_sum = 0
        total_sum += sum([order_product.get_product_sum() for order_product in self.products.all()])

        return total_sum

    # def get_quantity_of_all_products_in_order(self):
    #     total_quantity = 0
    #     total_quantity += sum([order_product.quantity for order_product in self.products.all()])
    #
    #     return total_quantity




