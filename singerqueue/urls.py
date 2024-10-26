from django.urls import path
from .views import HomePageView, BookMePageView, SingerQueueView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('queue/', SingerQueueView.as_view(), name='queue'),
    path('bookme', BookMePageView.as_view(), name='bookme'),
]
