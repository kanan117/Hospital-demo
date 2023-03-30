from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogs, Setting
from core.forms import ContactForm
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView

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



# view.py
from django.views.generic import ListView
from .models import Blogs, Setting

class BlogsListView(ListView):
    model = Blogs
    template_name = 'blog.html'
    context_object_name = 'blog'

    def get_queryset(self):
        return Blogs.objects.filter(is_published=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        return context


def blog_details(request, pk):
    context = {
        'title': 'blog',
        'blog': Blogs.objects.get(pk=pk)
    }
    return render(request, 'blog_details.html', context)



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

