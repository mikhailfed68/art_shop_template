from django.contrib import admin

from art_vostorg import models
from art_vostorg.froms import IventForm


@admin.register(models.Ivent)
class IventAdmin(admin.ModelAdmin):
    form = IventForm
