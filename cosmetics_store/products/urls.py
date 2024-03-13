from django.urls import path, include

from cosmetics_store.products.views import CreateProductView, EditProductView, DetailsProductView, DeleteProductView, \
    ListProductsView, ListBrandsView, list_brands

urlpatterns = (
    path("product/create/", CreateProductView.as_view(), name="create product"),
    path("product/<int:pk>/",
         include([
             path("edit/", EditProductView.as_view(), name="edit product"),
             path("details/", DetailsProductView.as_view(), name="details product"),
             path("delete/", DeleteProductView.as_view(), name="delete product"),
                ]),
         ),
    path("products/", ListProductsView.as_view(), name="list products"),
    # path("brands/", ListBrandsView.as_view(), name="list brands"),

    path("brands/", list_brands, name="list brands"),

)