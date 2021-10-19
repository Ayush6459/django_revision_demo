from django.shortcuts import render,HttpResponse
from .models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variables':"this is sent"
    }
    #messages.success(request,'This is a success message')
    return render(request,'index.html',context)
    #return HttpResponse('This is homepage')

def about(request):
    return render(request,'about.html')
    #return HttpResponse('This is about page')

def services(request):
    return render(request,'services.html')
    #return HttpResponse('This is services page')

def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone number')

        contact = Contact(username=username,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request,'Your contact has been saved')
    return render(request,'contact.html')
    #return HttpResponse('This is contact page')