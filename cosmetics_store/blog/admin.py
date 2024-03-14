from django.contrib import admin

from cosmetics_store.blog.models import ArticleModel


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    pass

