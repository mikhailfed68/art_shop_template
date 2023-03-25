from django.views.generic import ListView, DetailView, TemplateView

from art_vostorg import models


class IventListView(ListView):
    model = models.Ivent
    paginate_by = 6


class IventDetailView(DetailView):
    model = models.Ivent


class JoinToTeamView(TemplateView):
    template_name = 'art_vostorg/join.html'
