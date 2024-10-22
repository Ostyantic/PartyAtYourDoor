from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Singer
from accounts.models import CustomUser
from .forms import SingerForm


class HomePageView(CreateView, ListView):
    template_name = 'home.html'
    model = Singer
    form_class = SingerForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['singers'] = Singer.objects.all()
        context['custom_user'] = CustomUser.objects.all()
        return context


class SingerCreateView(CreateView):
    template_name = 'create_singer.html'
    model = Singer
    fields = ['name', 'song_name']


class BookMePageView(TemplateView):
    template_name = 'bookme.html'
