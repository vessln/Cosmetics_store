from django.db import models


class Brand(models.Model):
    MAX_BRAND_LENGTH = 40

    name = models.CharField(
        max_length=MAX_BRAND_LENGTH,
    )

    # creator = models.ForeignKey(
    #     Manager,
    #     on_delete=models.DO_NOTHING,
    #     related_name="created_brands",
    # )

