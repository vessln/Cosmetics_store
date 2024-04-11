from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models


UserModel = get_user_model()


class ArticleModel(models.Model):
    MAX_TITLE_LENGTH = 60
    MIN_TITLE_LENGTH = 3
    MAX_DESCRIPTION_LENGTH = 3000
    MIN_DESCRIPTION_LENGTH = 20
    MAX_URL_LENGTH = 1000

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

    article_image = models.URLField(
        max_length=MAX_URL_LENGTH,
        null=False,
        blank=False,
    )

    published_at = models.DateTimeField(
        auto_now_add=True,
    )

    author = models.ForeignKey(
        UserModel,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Article: {self.title}"

