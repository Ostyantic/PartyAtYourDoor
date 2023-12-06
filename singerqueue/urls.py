from django.urls import path
from .views import HomePageView, BookMePageView, SingerCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create/', SingerCreateView.as_view(), name='create_singer'),
    path('bookme', BookMePageView.as_view(), name='bookme'),
]
