from django.contrib.messages import views as messages_views
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as generic_views

from cosmetics_store.products.forms import CreateProductForm, UpdateProductForm
from cosmetics_store.products.mixin import ProductRestrictionMixin
from cosmetics_store.products.models import ProductModel


class CreateProductView(ProductRestrictionMixin, generic_views.CreateView):
    model = ProductModel
    form_class = CreateProductForm
    success_message = "The product was successfully added!"
    template_name = "products/create_product.html"

    def get_success_url(self):
        return reverse("details product", kwargs={"slug": self.object.slug})

    def form_valid(self, form):  # set currently authenticated user who create the product to `manager`
        form = super().form_valid(form)
        self.object.manager = self.request.user
        self.object.save()
        return form


class UpdateProductView(ProductRestrictionMixin, generic_views.UpdateView):
    model = ProductModel
    form_class = UpdateProductForm
    success_message = "The product was successfully edited!"
    template_name = "products/edit_product.html"

    def get_success_url(self):
        return reverse("details product", kwargs={"slug": self.object.slug})


class DetailsProductView(generic_views.DetailView):
    model = ProductModel
    template_name = "products/details_product.html"



class DeleteProductView(ProductRestrictionMixin, messages_views.SuccessMessageMixin, generic_views.DeleteView):
    model = ProductModel
    template_name = "products/delete_product.html"
    success_message = "The product was successfully deleted!"
    success_url = reverse_lazy("list products")


class ListProductsView(generic_views.ListView):
    queryset = ProductModel.objects.all()
    template_name = "products/list_products.html"

    @property
    def searched_word(self):
        return self.request.GET.get("searched_word", None)

    @property
    def searched_category(self):
        return self.request.GET.get("searched_category", None)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["searched_word"] = self.searched_word or ""
        context["searched_category"] = self.searched_category or ""

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        search_word = self.searched_word
        if search_word:
            queryset = ProductModel.objects.filter(
                Q(title_product__icontains=search_word) | Q(description__icontains=search_word)
            )

        search_category = self.searched_category
        if search_category:
            queryset = ProductModel.objects.filter(category=search_category)


        return queryset


class ListBrandsView(generic_views.ListView):
    # return flat list of unique values of the brand field:
    queryset = ProductModel.objects.order_by("brand").values_list("brand", flat=True).distinct()
    template_name = "products/list_brands.html"



