from django import forms
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from cosmetics_store.core.mixins import FormControlFieldsMixin
from cosmetics_store.products.models import ProductModel


class CreateProductForm(FormControlFieldsMixin, forms.ModelForm):
    fields_requiring_form_control = ("title_product", "category", "brand", "price", "description", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._make_fields_form_control()

    class Meta:
        model = ProductModel
        fields = ("title_product", "category", "brand", "price", "image_product", "description", )

        widgets = {
            "title_product": forms.TextInput(attrs={"placeholder": "Title of the product"}),
            "category": forms.RadioSelect(choices=ProductModel.PRODUCTS_CATEGORIES, ),
            "brand": forms.TextInput(attrs={"placeholder": "Brand of the product"}),
            "price": forms.NumberInput(attrs={"placeholder": "Price:  00.00"}),
            "description": forms.Textarea(attrs={
                "placeholder": "Write a product description...",
                "rows": 8,
                "cols": 55,
            }),
        }

        error_messages = {
            "category": {
                "required": "Please, select a category. This field is required.",
            },
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

        # makes brand's name UPPERCASE
        instance.brand = self.cleaned_data["brand"].upper()
        # makes title_product's name UPPERCASE
        instance.title_product = self.cleaned_data["title_product"].upper()

        image = self.cleaned_data["image_product"]
        img = Image.open(image)
        # thumbnail() calculates an appropriate thumbnail size to preserve the aspect of the image and resizes it:
        img.thumbnail((400, 400))

        # creates temporary object for the image, which is stored in memory, not on disk
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        # ensures that all data from the Beginning of the buffer will be ridden (pointer is moved to the beginning):
        buffer.seek(0)

        # updates the instance's image field with the new resized image
        instance.image_product = InMemoryUploadedFile(
            buffer,
            None,
            f"{image.name.split('.')[0]}_resized.jpg",
            "image/jpeg",   # MIME type
            buffer.getbuffer().nbytes,
            None
        )

        if commit:
            instance.save()
        return instance


class UpdateProductForm(FormControlFieldsMixin, forms.ModelForm):
    fields_requiring_form_control = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._make_fields_form_control()

        self.fields["title_product"].widget.attrs["readonly"] = "readonly"
        self.fields["brand"].widget.attrs["readonly"] = "readonly"

    class Meta:
        model = ProductModel
        fields = ("title_product", "brand", "price", "description",)

        error_messages = {
            "price": {
                "required": "Please, enter a price. This field is required.",
            },
            "description": {
                "required": "Please, write a product description. This field is required.",
            },
        }


