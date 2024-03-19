from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


PRODUCTS_CATEGORIES = [
    ("Make-up", "Make-up"),
    ("Skin care", "Skin care"),
    ("Hair care", "Hair care"),
    ("Personal Care", "Personal Care"),
]

MAX_DESCRIPTION_LENGTH = 500


# class Ingredient(models.Model):
#     MAX_NAME_LENGTH = 30
#
#     name = models.CharField(
#         MAX_NAME_LENGTH=30,
#     )
#     description = models.TextField(
#         max_length=MAX_DESCRIPTION_LENGTH,
#     )


# class Brand(models.Model):
#     MAX_NAME_LENGTH = 20
#
#     name = models.CharField(
#         max_length=MAX_NAME_LENGTH
#     )
#
#     class Meta:
#         ordering = ("name", )  #  the default ordering of Brand's records from DB should be based on the name field


class ProductModel(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_TYPE_LENGTH = 25
    MAX_BRAND_LENGTH = 20

    title_product = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=PRODUCTS_CATEGORIES,
        null=False,
        blank=False,
    )

    brand = models.CharField(
        max_length=MAX_BRAND_LENGTH,
        null=False,
        blank=False,
    )

    price = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=False,
        blank=False,
    )

    image_product = models.ImageField(
        upload_to="",
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=False,
        blank=False,
    )

    slug = models.SlugField()

    manager = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    # ingredients = models.ManyToManyField(
    #     Ingredient,
    #     on_delete=models.DO_NOTHING,
    # )

