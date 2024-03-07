from django.shortcuts import render
from django.views import generic as generic_views


class CreateProductView(generic_views.CreateView):
    pass


class EditProductView(generic_views.UpdateView):
    pass


class DetailsProductView(generic_views.DetailView):
    pass


class DeleteProductView(generic_views.DeleteView):
    pass


class ListProductsView(generic_views.ListView):
    pass


class ListBrandsView(generic_views.ListView):
    pass
