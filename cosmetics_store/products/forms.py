from django import forms
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from cosmetics_store.products.models import ProductModel


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ("title_product", "category", "brand", "price", "image_product", "description", )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.cleaned_data.get("image_product"):
            image = self.cleaned_data["image_product"]
            img = Image.open(image)
            img.thumbnail((300, 300))

            # Save the resized image to a BytesIO buffer
            buffer = BytesIO()
            img.save(buffer, format="JPEG")
            buffer.seek(0)

            # Update the instance's image field with the resized image
            instance.image_product = InMemoryUploadedFile(
                buffer,
                None,
                f'{image.name.split(".")[0]}_resized.jpg',
                'image/jpeg',
                buffer.getbuffer().nbytes,
                None
            )

        if commit:
            instance.save()
        return instance


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ("title_product", "category", "brand", "price", "image_product", "description",)


