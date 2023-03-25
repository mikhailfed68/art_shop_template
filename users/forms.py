from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_picture",
            "about_me",
        ]

    def clean_profile_picture(self):
        picture = self.cleaned_data.get("profile_picture", False)
        if picture:
            width, height = get_image_dimensions(picture)
            if (width < 150) or (height < 150):
                raise ValidationError(
                    """
                    Слишком маленькое изображение,
                    минимальная высота и ширина - 150 пикселей.
                    """
                )
            elif (width > 2500 or (height > 2500)):
                raise ValidationError(
                    """
                    Слишком большое изображение,
                    максимальная высота и ширина - 2500x2500 пикселей.
                    """
                )
        return picture
