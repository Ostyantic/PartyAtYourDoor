from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Singer
from .forms import SingerForm


class HomePageView(CreateView, ListView):
    template_name = 'home.html'
    model = Singer
    form_class = SingerForm
    context_object_name = 'singers'
    success_url = reverse_lazy("home")


class SingerCreateView(CreateView):
    template_name = 'create_singer.html'
    model = Singer
    fields = ['name', 'song_name']


class BookMePageView(TemplateView):
    template_name = 'bookme.html'
