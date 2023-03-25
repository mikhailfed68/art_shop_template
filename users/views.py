from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.db.transaction import atomic
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import BaseDeleteView

from users.forms import CustomUserChangeForm, SignUpForm
from users import services


@method_decorator(decorator=atomic, name="dispatch")
class SiqnUp(CreateView):
    """Registers the user on the site."""

    model = get_user_model()
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        user = form.save()
        services.add_user_to_base_group_or_create_one(user)
        login(self.request, user)
        messages.success(self.request, "Вы успешно зарегестрированы!")
        return redirect(self.success_url)


class ProfileDetailView(DetailView):
    """
    Return the user profile by the 'username' slug
    and its published articles list.
    """

    model = get_user_model()
    template_name = "users/profile.html"
    context_object_name = 'member'
    slug_field = "username"
    slug_url_kwarg = "username"


class UserListView(ListView):
    """Rerturn the registred users list."""

    model = get_user_model()
    paginate_by = 6


@method_decorator(decorator=atomic, name="dispatch")
class UserUpdateView(
    UserPassesTestMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView
):
    """Update User data."""

    permission_required = "users.change_user"

    model = get_user_model()
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/update_user.html"
    form_class = CustomUserChangeForm

    success_message = "Вы успешно обновили свои данные."

    def test_func(self):
        "Verify user identity by session user object"
        return self.request.user.get_username() == self.kwargs.get("username")


@method_decorator(decorator=atomic, name="dispatch")
class UserDestroyView(
    UserPassesTestMixin, PermissionRequiredMixin, SuccessMessageMixin, BaseDeleteView
):
    """Delete user."""

    permission_required = "users.delete_user"

    model = get_user_model()
    slug_field = "username"
    slug_url_kwarg = "username"
    success_url = settings.LOGOUT_REDIRECT_URL

    success_message = "Аккаунт успешно удален"

    def test_func(self):
        "Verify user identity by session user object"
        return self.request.user.get_username() == self.kwargs.get("username")
