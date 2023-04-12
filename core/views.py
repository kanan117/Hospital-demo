from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Blogs, Doctors, Setting, Subscriber
from core.forms import ContactForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models import Q
from baseuser.models import BaseUser
from celery import shared_task
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.db.models import Q
from .models import Subscriber, Setting,  Contact



# Create your views here.
def home(request):
  context = {'setting': Setting.objects.first()}
  return render(request, 'home.html', context)


def about(request):
  context = {
    'setting': Setting.objects.first(),
  }
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
  paginate_by = 2

  def get_queryset(self):
    return Blogs.objects.filter(is_published=True)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['setting'] = Setting.objects.first()
    return context

  def get_paginate_by(self, queryset):
    paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
    if paginate_by:
      return int(paginate_by)
    return self.paginate_by


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
    return context

  def get_paginate_by(self, queryset):
    paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
    if paginate_by:
      return int(paginate_by)
    return self.paginate_by


def blog_details(request, slug):
  blog = Blogs.objects.get(slug=slug)
  context = {'blog': blog, 'setting': Setting.objects.first()}
  return render(request, 'blog_details.html', context)


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
  context = {
    'doctors': doctors,
    'query': query,
    'setting': Setting.objects.first()
  }
  return render(request, 'search_doctors.html', context)


# @shared_task
# @user_passes_test(lambda u: u.has_perm('subscriber.can_send_email'))
# def send_mail_to_subscribers():
#     subscribers = Subscriber.objects.filter(is_active=True)
#     subscriber_emails = subscribers.values_list('email', flat=True)
#     return subscriber_emails

@shared_task
@user_passes_test(lambda u: u.has_perm('subscriber.can_send_email'))
def send_email(request):
    setting = Setting.objects.first()

    if request.method == 'POST':
        recipient_list = []
        to_subscribers = request.POST.get('to_subscribers')
        to_baseusers = request.POST.get('to_baseusers')
        to_contacts = request.POST.get('to_contacts')
        subject = request.POST['subject']
        message = request.POST['message']
        sender = 'your-email@example.com'

        if 'recipient_list[]' in request.POST:
            recipient_list = request.POST.getlist('recipient_list[]')

        if to_subscribers:
            subscribers = Subscriber.objects.filter(is_active=True)
            subscriber_emails = subscribers.values_list('email', flat=True)
            recipient_list += list(subscriber_emails)

        if to_baseusers:
            baseuser_emails = BaseUser.objects.filter(Q(is_active=True) & Q(email__isnull=False)).values_list('email', flat=True)
            recipient_list += list(baseuser_emails)

        if to_contacts:
            contact_emails = Contact.objects.filter(Q(email__isnull=False)).values_list('email', flat=True)
            recipient_list += list(contact_emails)

        recipient_list = list(set(recipient_list))

        send_mail(
            subject,
            message,
            sender,
            recipient_list,
            fail_silently=False,
        )

        context = {'message': 'Email has been sent successfully!', 'setting': setting}
        return render(request, 'email_sent.html', context)

    return render(request, 'send_email.html', {'setting': setting})
