from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request, "Test==========")
    # return HttpResponse("Aisha")
    return render(request, 'index.html')
def about(request):
    messages.success(request, "About message")
    return render(request, 'about.html')  

def services(request):
    return render(request, 'services.html')   

def contact(request):
    if request.method == 'POST':
        print("printing post request:------------",request.POST)
        name= request.POST.get('name')
        email= request.POST.get('email')
        # password= request.POST.get('password')
        address=request.POST.get('address')
        contact=Contact(name=name, email=email, address=address)
        contact.save()
        messages.success(request, 'Contact Saved')
        
        
    return render(request, 'contact.html')    