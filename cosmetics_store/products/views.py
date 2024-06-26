from django.contrib.messages import views as messages_views
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as generic_views

from cosmetics_store.core.user_mixins import PageRestrictionMixin
from cosmetics_store.products.forms import CreateProductForm, UpdateProductForm, FilterProductForm
from cosmetics_store.products.models import ProductModel


class CreateProductView(PageRestrictionMixin, generic_views.CreateView):
    model = ProductModel
    form_class = CreateProductForm
    success_message = "The product was successfully added!"
    template_name = "products/create_product.html"

    def get_success_url(self):
        return reverse("details product", kwargs={"slug": self.object.slug})

    def form_valid(self, form):  # set currently authenticated user who create the product to `manager`
        form = super().form_valid(form)
        self.object.user = self.request.user
        self.object.save()
        return form


class UpdateProductView(PageRestrictionMixin, generic_views.UpdateView):
    model = ProductModel
    form_class = UpdateProductForm
    success_message = "The product was successfully edited!"
    template_name = "products/edit_product.html"

    def get_success_url(self):
        return reverse("details product", kwargs={"slug": self.object.slug})


class DetailsProductView(generic_views.DetailView):
    model = ProductModel
    template_name = "products/details_product.html"


class DeleteProductView(PageRestrictionMixin, messages_views.SuccessMessageMixin, generic_views.DeleteView):
    model = ProductModel
    template_name = "products/delete_product.html"
    success_message = "The product was successfully deleted!"
    success_url = reverse_lazy("list products")


class ListProductsView(generic_views.ListView):
    queryset = ProductModel.objects.order_by("-created_at")
    template_name = "products/list_products.html"

    @property
    def searched_product(self):
        return self.request.GET.get("searched_product", None)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["searched_product"] = self.request.GET.get("searched_product", None) or ""
        context["filter_products"] = FilterProductForm(self.request.GET)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        search_product = self.request.GET.get("searched_product", None) or ""

        if search_product:
            queryset = ProductModel.objects.filter(
                Q(title_product__icontains=search_product))


        form = FilterProductForm(self.request.GET)
        if form.is_valid():
            category = form.cleaned_data.get("category")
            min_price = form.cleaned_data.get("min_price")
            max_price = form.cleaned_data.get("max_price")
            brand = form.cleaned_data.get("brand")

            if category:
                queryset = queryset.filter(category=category)
            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
            if brand:
                queryset = queryset.filter(brand__icontains=brand)

        return queryset


class ListBrandsView(generic_views.ListView):
    template_name = "products/list_brands.html"

    def get_queryset(self):
        queryset = ProductModel.objects.all()
        searched_brand = self.request.GET.get("brand")

        if searched_brand:
            queryset = queryset.filter(brand__exact=searched_brand)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["all_brands"] = ProductModel.objects.order_by("brand").values_list("brand", flat=True).distinct()

        return context



