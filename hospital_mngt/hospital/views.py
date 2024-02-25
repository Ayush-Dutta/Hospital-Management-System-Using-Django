from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def About(request):
    return HttpResponse("<h1>this is the about section</h1>")