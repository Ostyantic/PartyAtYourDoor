from django.urls import path
from .views import HomePageView, BookMePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('bookme', BookMePageView.as_view(), name='bookme'),
]
