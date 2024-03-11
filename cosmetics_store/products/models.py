from django.db import models


PRODUCTS_CATEGORIES = [
    ("Make-up", "Make-up"),
    ("Skin care", "Skin care"),
    ("Hair care", "Hair care"),
    ("Other", "Other"),
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


# class Product(models.Model):
#     MAX_TITLE_LENGTH = 30
#     MAX_TYPE_LENGTH = 25
#     MAX_BRAND_LENGTH = 20
#
#     title_product = models.CharField(
#         max_length=MAX_TITLE_LENGTH
#     )
#
#     category = models.CharField(
#         max_length=MAX_TYPE_LENGTH,
#         choices=PRODUCTS_CATEGORIES,
#     )
#
#     price = models.DecimalField(
#         max_digits=3,
#         decimal_places=2,
#     )
#
#     image_product = models.ImageField(
#         upload_to="",
#     )
#
#     description = models.TextField(
#         max_length=MAX_DESCRIPTION_LENGTH,
#     )
#
#     brand = models.ForeignKey(
#         Brand,
#         on_delete=models.DO_NOTHING,
#     )
#
#     slug = models.SlugField()
#
#     ingredients = models.ManyToManyField(
#         Ingredient,
#         on_delete=models.DO_NOTHING,
#     )
#
#     creator = models.ForeignKey(
#         Manager,
#         on_delete=models.DO_NOTHING,
#         related_name="created_products",
#     )

