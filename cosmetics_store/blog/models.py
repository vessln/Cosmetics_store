from django.core.validators import MinLengthValidator
from django.db import models


class Article(models.Model):
    MAX_TITLE_LENGTH = 50
    MIN_TITLE_LENGTH = 3

    MAX_DESCRIPTION_LENGTH = 3000
    MIN_DESCRIPTION_LENGTH = 20

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=[
            MinLengthValidator(MIN_TITLE_LENGTH),
        ],
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=[
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ],
        null=False,
        blank=False,
    )

    article_image = models.ImageField(
        upload_to="article_image/",
        null=False,
        blank=False,
    )

    published_at = models.DateTimeField(
        auto_now_add=True,
    )

    # author = models.ForeignKey(
    #     Manager - user,
    #     on_delete=models.CASCADE,
    #     related_name=articles,
    # )

