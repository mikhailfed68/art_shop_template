import datetime

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

from sorl import thumbnail
from tinymce.models import HTMLField


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        abstract = True


def get_user_directory_path(instance, filename):
    return f"users/user_{instance.author.id}/ivent_{instance.id}/{filename}"


class Ivent(TimeStampedModel):
    "Article of blog."

    title = models.CharField("Заголовок", max_length=100, unique=True)
    title_photo = thumbnail.ImageField(
        "Фото", upload_to=get_user_directory_path, blank=True, null=True
    )
    description = models.CharField("Описание", max_length=256)
    body = HTMLField("Содержание")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Автор", null=True, on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("art_vostorg:ivent_detail", kwargs={"pk": self.pk})

    def was_updated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.updated_at
