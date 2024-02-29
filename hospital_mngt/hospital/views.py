from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def About(request):
    return render(request, 'about.html')
    #return HttpResponse("<h1>this is the about section</h1>")
    
def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')