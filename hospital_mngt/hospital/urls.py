from django.urls import path
from .views import About, Home

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
]