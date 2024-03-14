from django import forms
from django.contrib.auth import get_user_model

from cosmetics_store.blog.models import ArticleModel

UserModel = get_user_model()


class CustomBaseArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ("title", "description", "article_image", "author")

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Article title"}),
            "author": forms.HiddenInput(),

            "description": forms.Textarea(attrs={
                "placeholder": "Write the content here...",
                "rows": 10,
                "cols": 60,
            }),

        }

        error_messages = {
            "title": {
                "required": "Please, enter a required. This field is required.",
            },
            "description": {
                "required": "Please, enter description. This field is required.",
            },
            "article_image": {
                "required": "Please, add an suitable image. This field is required.",
            },
        }


class CreateArticleForm(CustomBaseArticleForm):
    pass


class UpdateArticleForm(CustomBaseArticleForm):
    CustomBaseArticleForm.Meta.exclude = ("article_image", "author")

    # class Meta:
    #     model = ArticleModel
    #     fields = ("title", "description",)
