from django.contrib import admin

from art_vostorg import models
from art_vostorg.froms import IventForm


@admin.register(models.Ivent)
class IventAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'author')
    search_help_text = 'Поиск по заголовку или описанию'
    search_fields = ('title', 'description', 'author__username')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 20
    form = IventForm
    autocomplete_fields = ('author',)
