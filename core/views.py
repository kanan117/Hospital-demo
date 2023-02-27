from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
    }
    return render(request,'home.html',context)

def about(request):
    context = {
    }
    return render(request,'about.html',context)

def appointment(request):
    context = {
    }
    return render(request,'appointment.html',context)

def base(request):
    context = {
    }
    return render(request,'base.html',context)
def blog_details(request):
    context = {
    }
    return render(request,'blog-details.html',context)
def booking_list(request):
    context = {
    }
    return render(request,'booking-list.html',context)
def contact(request):
    context = {
    }
    return render(request,'contact.html',context)
def doctor_details(request):
    context = {
    }
    return render(request,'doctor-details.html',context)
def doctor(request):
    context = {
    }
    return render(request,'doctor.html',context)
def doctors(request):
    context = {
    }
    return render(request,'doctors.html',context)
def error(request):
    context = {
    }
    return render(request,'error.html',context)
def faq(request):
    context = {
    }
    return render(request,'faq.html',context)
def index_2(request):
    context = {
    }
    return render(request,'index-2.html',context)
def login(request):
    context = {
    }
    return render(request,'login.html',context)
def service_details(request):
    context = {
    }
    return render(request,'service-details.html',context)
def service(request):
    context = {
    }
    return render(request,'service.html',context)
def services(request):
    context = {
    }
    return render(request,'services.html',context)
