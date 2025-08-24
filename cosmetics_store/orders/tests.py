from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

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


@override_settings(SECRET_KEY="tests-secret-key", PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"])
class OrdersCartViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = create_user()
        self.client.login(username=self.user.username, password="pass1234")
        self.product = create_product()

    def test_add_product_creates_order_and_item(self):
        url = reverse("add to cart", args=[self.product.slug])
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)

        order = OrderModel.objects.filter(user=self.user, is_ordered=False).first()
        self.assertIsNotNone(order)
        self.assertEqual(order.products.count(), 1)

        op = order.products.first()
        self.assertEqual(op.product, self.product)
        self.assertEqual(op.user, self.user)
        self.assertEqual(op.quantity, 1)

    def test_add_same_product_increments_quantity_up_to_10(self):
        url = reverse("add to cart", args=[self.product.slug])
        for _ in range(3):
            self.client.get(url)
        op = OrderProductModel.objects.get(user=self.user, product=self.product, is_ordered=False)
        self.assertEqual(op.quantity, 3)

        for _ in range(20):
            self.client.get(url)
        op.refresh_from_db()
        self.assertEqual(op.quantity, 10)

    def test_remove_product_deletes_item_and_empty_order(self):
        op = OrderProductModel.objects.create(product=self.product, user=self.user, quantity=1, is_ordered=False)
        order = OrderModel.objects.create(user=self.user, is_ordered=False)
        order.products.add(op)

        url = reverse("remove from cart", args=[self.product.slug])
        resp = self.client.get(url, follow=True)
#
