from django.views.generic import TemplateView, ListView, CreateView
from .models import Singer

class HomePageView(ListView):
    template_name = 'home.html'
    model = Singer
    context_object_name = 'singers'

class SingerCreateView(CreateView):
    template_name = 'create_singer.html'
    model = Singer
    fields = ['name', 'song_name']



class BookMePageView(TemplateView):
    template_name = 'bookme.html'
