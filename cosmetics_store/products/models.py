from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


# class Ingredient(models.Model):
#     MAX_NAME_LENGTH = 30
#
#     name = models.CharField(
#         MAX_NAME_LENGTH=30,
#     )
#     description = models.TextField(
#         max_length=MAX_DESCRIPTION_LENGTH,
#     )


class ProductModel(models.Model):
    PRODUCTS_CATEGORIES = [
        ("Make-up", "Make-up"),
        ("Skin care", "Skin care"),
        ("Hair care", "Hair care"),
        ("Personal Care", "Personal Care"),
    ]

    MAX_TITLE_LENGTH = 30
    MAX_TYPE_LENGTH = 25
    MAX_BRAND_LENGTH = 20
    MAX_DESCRIPTION_LENGTH = 800
    MAX_INGREDIENTS_LENGTH = 300

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
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
    )

    image_product = models.ImageField(
        upload_to="products_image/",
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=False,
        blank=False,
    )

# TODO: make ingredients logic
    # ingredients = models.TextField(
    #     max_length=MAX_INGREDIENTS_LENGTH,
    #     null=False,
    #     blank=False,
    # )

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
    )

    manager = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title_product

    # ingredients = models.ManyToManyField(
    #     Ingredient,
    #     on_delete=models.DO_NOTHING,
    # )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.brand}-{self.title_product}-{self.pk}")
            # slugify(f"nyx"-"glam palette"-"3") -> "nyx-glam-palette-3"

        super().save(*args, **kwargs)

