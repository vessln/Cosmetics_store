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


def list_brands(request):
    context = {
        "brand1": "Asdfsfs",
        "brand2": "Agolkl rhtrt",
        "brand3": "Brascfaa as",
        "brand4": "Csakgsd",
        "brand5": "Dhasfija",
    }

    return render(request, "products/list_brands.html", context)

