from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Singer, ContactInfo
from accounts.models import CustomUser
from .forms import SingerForm, ContactForm


class HomePageView(CreateView, ListView):
    guest_id = ''
    template_name = 'home.html'
    model = ContactInfo
    form_class = ContactForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['guest_id'] = self.guest_id
        context['contacts'] = ContactInfo.objects.all()
        context['admin'] = CustomUser.objects.get(id=1)
        return context


class SingerQueueView(CreateView, ListView):
    template_name = 'singer_queue.html'
    model = Singer
    form_class = SingerForm
    context_object_name = 'singers'
    success_url = reverse_lazy("home")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['guest_id'] = self.guest_id
    #     context['singers'] = Singer.objects.all()
    #     context['admin'] = CustomUser.objects.get(id=1)
    #     return context


class BookMePageView(TemplateView):
    template_name = 'bookme.html'
