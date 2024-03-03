from django.urls import path
from .views import About, Home, Contact, Login, Logout_admin
urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='login'),
    path('logout/', Logout_admin, name='logout_admin'),
]