from datetime import timedelta

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.core.cache import cache
from django.db import models
from django.urls import reverse
from django.utils import timezone
from sorl import thumbnail


def get_user_directory_path(instance, filename):
    return f"users/user_{instance.id}/profile_picture/{filename}"


class User(AbstractUser):
    """A user model."""

    username = models.CharField(
        "Имя пользователя",
        help_text="""
        Обязательное поле. Не более 10 символов.
        только буквы, цифры и символы @/./+/-/_.
        """,
        unique=True,
        max_length=10,
    )
    email = models.EmailField(
        "Электронный адрес",
        help_text="Почта должна быть уникальной.",
        error_messages={"unique": "Электронная почта уже используется."},
        unique=True,
    )
    profile_picture = thumbnail.ImageField(
        "Фото пользователя", upload_to=get_user_directory_path, blank=True, null=True
    )
    about_me = models.CharField("О себе", max_length=60, blank=True, null=True)

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return self.get_username()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"username": self.username})

    def last_seen(self):
        return cache.get(f"last_seen_{self.id}")

    @admin.display(
        boolean=True,
        description='В сети',
    )
    def is_online(self):
        last_seen = self.last_seen()
        if last_seen:
            now = timezone.now()
            if now > last_seen + timedelta(seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            return True
        return False
