from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as generic_views

from cosmetics_store.products.forms import CreateProductForm, UpdateProductForm
from cosmetics_store.products.models import ProductModel


class CreateProductView(generic_views.CreateView):
    model = ProductModel
    form_class = CreateProductForm
    template_name = "products/create_product.html"

    def get_success_url(self):
        return reverse("details product", kwargs={"slug": self.object.slug})

    def form_valid(self, form):  # set currently authenticated user who create the product to `manager`
        form = super().form_valid(form)
        self.object.manager = self.request.user
        self.object.save()
        return form


class UpdateProductView(generic_views.UpdateView):
    model = ProductModel
    form_class = UpdateProductForm
    template_name = "products/edit_product.html"

    def get_success_url(self):
        return reverse("details product", kwargs={"slug": self.object.slug})


class DetailsProductView(generic_views.DetailView):
    model = ProductModel
    template_name = "products/details_product.html"


class DeleteProductView(generic_views.DeleteView):
    model = ProductModel
    template_name = "products/delete_product.html"
    success_url = reverse_lazy("list products")


class ListProductsView(generic_views.ListView):
    queryset = ProductModel.objects.all()
    template_name = "products/list_products.html"


class ListBrandsView(generic_views.ListView):
    # return flat list of unique values of the brand field:
    queryset = ProductModel.objects.order_by("brand").values_list("brand", flat=True).distinct()
    template_name = "products/list_brands.html"



