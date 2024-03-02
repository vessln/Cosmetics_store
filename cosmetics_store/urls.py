from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("cosmetics_store.common.urls")),
    path("accounts/", include("cosmetics_store.accounts.urls")),
    path("blog/", include("cosmetics_store.blog.urls")),
    path("brands/", include("cosmetics_store.brands.urls")),

]
