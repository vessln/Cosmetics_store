from django.contrib import admin

from cosmetics_store.blog.models import ArticleModel


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "article_image", "published_at", "author")
    list_filter = ("title", "published_at", "author")
    ordering = ("published_at", )
    search_fields = ("title", "published_at", "author")
    fieldsets = (
        ("Main info", {"fields": ("author", ), }),
        ("Article details", {"fields": ("title", "description", ), })
    )


