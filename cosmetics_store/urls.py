from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("cosmetics_store.common.urls")),
    path("accounts/", include("cosmetics_store.accounts.urls")),
    path("blog/", include("cosmetics_store.blog.urls")),
    path("shop/", include("cosmetics_store.products.urls")),
    path("orders/", include("cosmetics_store.orders.urls")),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)