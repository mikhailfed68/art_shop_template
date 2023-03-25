from django.urls import path
from django.views.generic.base import RedirectView

from art_vostorg import views

app_name = 'art_vostorg'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name="art_vostorg:ivent_list", permanent=True)),
    path('ivents/', views.IventListView.as_view(), name='ivent_list'),
    path('ivents/<int:pk>/', views.IventDetailView.as_view(), name='ivent_detail'),
    path('join/', views.JoinToTeamView.as_view(), name='join'),
]
