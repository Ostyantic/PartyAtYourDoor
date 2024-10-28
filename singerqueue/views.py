from django.views.generic import TemplateView, CreateView, ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Singer, ContactInfo
from accounts.models import CustomUser
from .forms import SingerForm, ContactForm
from django.http import JsonResponse


class HomePageView(CreateView, FormView):
    guest_id = ''
    template_name = 'home.html'
    model = ContactInfo
    form_class = ContactForm
    success_url = reverse_lazy("queue")

    def form_valid(self, form):
        # This method is called when the form is valid
        return super().form_valid(form)  # This will redirect to success_url

    def form_invalid(self, form):
        # This method is called when the form is invalid
        return super().form_invalid(form)  # This will re-render the form with errors

    # Commented out error for login page, will come back to later

    # def form_invalid(self, form):
    #     # Check if the request is AJAX
    #     if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #         return JsonResponse({"errors": form.errors}, status=400)
    #     return super().form_invalid(form)

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
    success_url = reverse_lazy("queue")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['guest_id'] = self.guest_id
    #     context['singers'] = Singer.objects.all()
    #     context['admin'] = CustomUser.objects.get(id=1)
    #     return context


class BookMePageView(TemplateView):
    template_name = 'bookme.html'
