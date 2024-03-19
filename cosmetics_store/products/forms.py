from django import forms
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from cosmetics_store.products.models import ProductModel


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ("title_product", "category", "brand", "price", "image_product", "description", )

