from django.test import TestCase
from unittest.mock import patch
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from django.utils import timezone
import uuid

from cosmetics_store.orders.models import (
    OrderModel,
    OrderProductModel,
    UserShippingAddressModel,
)
from cosmetics_store.products.models import ProductModel



User = get_user_model()


def create_user(username="VeskaTest", **extra):
    defaults = dict(
        username=username,
        email=f"{username}@example.com",
        first_name="Veska",
        last_name="Test",
        password="pass1234",
        is_staff=False,
        is_superuser=False,
    )
    defaults.update(extra)
    user = User.objects.create_user(**defaults)
    if hasattr(user, "phone") and not getattr(user, "phone"):
        setattr(user, "phone", "0888123456")
        user.save(update_fields=["phone"])
    return user


def create_product(
    title="Serum X",
    category="face",
    brand="niwea",
    slug=None,
    price=29.90,
    description="this is hydrating face serum.",
    sales_count=0,
    **extra,
):
    obj = ProductModel(
        title_product=title,
        slug=slug,
        category=category,
        brand=brand,
        price=price,
        description=description,
        sales_count=sales_count,
        **extra,
    )
    obj.save()
    return obj



class OrdersModelsTests(TestCase):
    def setUp(self):
        self.user = create_user()
        self.product = create_product(price=12.5)

    def test_order_product_str(self):
        op = OrderProductModel.objects.create(
            product=self.product,
            user=self.user,
            quantity=3,
            is_ordered=False,
        )
        self.assertEqual(str(op), f"Product: {self.product.title_product}, count: 3")

    def test_get_product_sum(self):
        op = OrderProductModel.objects.create(
            product=self.product,
            user=self.user,
            quantity=4,
            is_ordered=False,
        )
        self.assertEqual(op.get_product_sum(), 4 * 12.5)





