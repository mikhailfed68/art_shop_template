from django.utils.html import format_html, html_safe
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import CustomUserChangeForm
from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['avatar', 'bold_username', 'is_online', 'email', 'first_name', 'last_name', 'is_staff']
    list_display_links = ['avatar', 'bold_username']
    list_filter = ('groups', 'is_staff', 'is_superuser')
    search_fields = ('bold_username',)
    autocomplete_fields = ('groups',)
    form = CustomUserChangeForm  # adding validation for profile_picture field

    @admin.display(description='Username', ordering='username')
    def bold_username(self, object):
        return format_html(f'<b>{object.username}</b>')

    @admin.display(description='Аватар')
    def avatar(self, object):
        if object.profile_picture:
            return format_html(
                f'<img src="{object.profile_picture.url}" width="60" height="60" alt="profile-picture" style="border-radius: 30px;"/>'
            )
        return ''
