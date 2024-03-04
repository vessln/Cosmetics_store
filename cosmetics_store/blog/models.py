from django.db import models


class Article(models.Model):
    MAX_TITLE_LENGTH = 50
    MAX_DESCRIPTION_LENGTH = 3000

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=False,
        blank=False,
    )

    article_image = models.ImageField(
        upload_to="",
        validators=[],
        null=False,
        blank=False,
    )

    published_at = models.DateTimeField(
        auto_now_add=True,
    )

    # author = models.ForeignKey(
    #     user,
    #     on_delete=models.CASCADE,
    #     related_name=articles,
    # )

