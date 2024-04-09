from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class RegisterUserViewTests(TestCase):
    def create_store_user(self):
        return UserModel.objects.create_user(username="Veskata", password="12345")

    def test_successful_login_template_code_get_create_storeuser(self):
        self.create_store_user()
        self.client.login(username="Veskata", password="12345")

        response = self.client.get(reverse("home page"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/home_page.html")

    def test_successful_register_template_code_get_create_storeuser(self):
        self.create_store_user()

        response = self.client.get(reverse("register user"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register_user.html")

