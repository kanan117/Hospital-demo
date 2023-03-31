from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Blogs, Doctors, Setting
from core.forms import ContactForm


def my_custom_permission_denied_view(request, exception=None):
  return render(request, 'error.html', {})


# Create your views here.
def home(request):
  context = {'setting': Setting.objects.first()}
  return render(request, 'home.html', context)


def about(request):
  context = {'setting': Setting.objects.first(),}
  return render(request, 'about.html', context)


def appointment(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'appointment.html', context)


def base(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'base.html', context)


def blog_details(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'blog_details.html', context)


def booking_list(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'booking_list.html', context)


def contact(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'contact.html', context)


def doctor_details(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'doctor_details.html', context)


def doctor(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'doctor.html', context)


def doctors(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'doctors.html', context)


def error(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'error.html', context)


def faq(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'faq.html', context)


def index_2(request):
  context = {'title': 'None', 'setting': Setting.objects.first()}
  return render(request, 'index_2.html', context)


def service_details(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'service_details.html', context)


def service(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'service.html', context)


def services(request):
  context = {
    'setting': Setting.objects.first(),
  }
  return render(request, 'services.html', context)





class BlogsListView(ListView):
  model = Blogs
  template_name = 'blog.html'
  context_object_name = 'blog'
  paginate_by = 3

  def get_queryset(self):
    return Blogs.objects.filter(is_published=True)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['setting'] = Setting.objects.first()
    return context

  def get_paginate_by(self, queryset):
    return self.request.GET.get('paginate_by', self.paginate_by)




def blog_details(request, slug):
  blog = Blogs.objects.get(slug=slug)
  context = {'blog': blog, 'setting': Setting.objects.first()}
  return render(request, 'blog_details.html', context)




class DoctorsListView(ListView):
    model = Doctors
    template_name = 'doctor.html'
    context_object_name = 'doctor'
    paginate_by = 6

    def get_queryset(self):
        return Doctors.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()

        # Retrieve doctors queryset and create a paginator
        doctors_queryset = self.get_queryset()
        paginator = Paginator(doctors_queryset, self.paginate_by)

        # Get current page number from the request query parameters
        page_number = self.request.GET.get('page')

        # Get the page object for the current page number
        current_page = paginator.get_page(page_number)

        # Add current page and paginator object to the context
        context['page_obj'] = current_page
        context['paginator'] = paginator

        return context


def doctor_details(request, slug):
  doctor = Doctors.objects.get(slug=slug)
  context = {'doctor': doctor, 'setting': Setting.objects.first()}
  return render(request, 'doctor_details.html', context)



def contact(request):
  form = ContactForm()
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      form = ContactForm()

  context = {
    'setting': Setting.objects.first(),
    'contact': form,
  }
  return render(request, 'contact.html', context)



def search_doctors(request):
    query = request.GET.get('q')
    if query:
        doctors = Doctors.objects.filter(name__icontains=query)
    else:
        doctors = []
    context = {'doctors': doctors, 'query': query , 'setting': Setting.objects.first()}
    return render(request, 'search_doctors.html', context )
