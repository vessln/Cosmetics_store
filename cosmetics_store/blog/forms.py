from django import forms
from django.contrib.auth import get_user_model

from cosmetics_store.blog.models import ArticleModel
from cosmetics_store.core.mixins import FormControlFieldsMixin

UserModel = get_user_model()


class CustomBaseArticleForm(FormControlFieldsMixin, forms.ModelForm):
    fields_requiring_form_control = ("title", "description",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._make_fields_form_control()

    class Meta:
        model = ArticleModel
        fields = ("title", "description", "article_image", "author")

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Title of the article"}),
            "author": forms.HiddenInput(),

            "description": forms.Textarea(attrs={
                "placeholder": "Write the content here...",
                "rows": 10,
                "cols": 65,
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
