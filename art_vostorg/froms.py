from django import forms
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

from art_vostorg.models import Ivent



class IventForm(forms.ModelForm):
    class Meta:
        model = Ivent
        fields = ["title", "description", "title_photo", "body", "author"]

    def clean_title_photo(self):
        title_photo = self.cleaned_data.get("title_photo")

        if title_photo:
            width, height = get_image_dimensions(title_photo)
            if (width < 512) or (height < 512):
                raise ValidationError(
                    """
                    Слишком маленькое изображение,
                    минимальная высота и ширина - 512x512 пикселей.
                    """
                )
            elif (width > 2500) or (height > 2500):
                raise ValidationError(
                    """Слишком большое изображение,
                    максимальная высота и ширина - 2500x2500 пикселей.
                    """
                )
        return title_photo
