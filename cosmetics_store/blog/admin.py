from django.contrib import admin

from cosmetics_store.blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

