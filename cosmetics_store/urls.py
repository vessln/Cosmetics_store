from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("cosmetics_store.common.urls")),
    path("accounts/", include("cosmetics_store.accounts.urls")),
    path("blog/", include("cosmetics_store.blog.urls")),
    path("shop/", include("cosmetics_store.products.urls")),
    path("orders/", include("cosmetics_store.orders.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
#     ]