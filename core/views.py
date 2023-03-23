from django.shortcuts import render
from django.http import HttpResponse

from .models import Blogs, Setting
from core.forms import ContactForm
from django.urls import reverse

from django.shortcuts import render
from django.contrib import messages
# from .forms import SubscribeForm
# from .models import Subscriber
from django.shortcuts import render

def my_custom_permission_denied_view(request, exception=None):
    return render(request, 'error.html', {})

# Create your views here.
def home(request):
  context = {'setting': Setting.objects.first()}
  return render(request, 'home.html', context)


def about(request):
  blogs = Blogs.objects.first()
  context = {'setting': Setting.objects.first(), "blogs": blogs}
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


# def Blog(request):
#     context = {
#         'title' : "Blogs",
#         'blogs' : Blog.objects.all()
#     }
#     return render(request, 'blog.html', context)
# django


def blog(request):
  blogs = Blogs.objects.filter(is_published=False).order_by('created_at')
  context = {'setting': Setting.objects.first(), 'blogs': blogs}
  return render(request, 'blog.html', context)


def blog_details(request, id):
  blogs = Blogs.objects.get(id=id)
  context = {'setting': Setting.objects.first(), 'blogs': blogs}
  return render(request, 'blog_details.html', context)


# def blogs(request, pk):
#     context = {
#         'title' : 'Blogs',
#         'blogs' : Blogs.objects.get(id=pk)
#     }
#     return render(request, 'blogs.html', context)

# def contact(request):
#     context = {
#         'title' : "Contact",
#         'contact' : ContactForm()
#     }
#     if request.method  == 'post':
#         form = ContactForm(request.post)
#         if form.is_valid():
#             form.save()
#             return HttpResponse(reverse('home'))
#     return render(request, 'contact.html', context)


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




# def Subscribe(request):
#     form = SubscribeForm(request.POST)

#     if form.is_valid():
#         email = form.cleaned_data['email']
#         new_subscriber = Subscriber.objects.create(email=email)
#         messages.success(request, 'Thanks for subscribing!')

# from django.shortcuts import render
# from django.core.mail import send_mail
# from django.template.loader import render_to_string

# def send_email(request):
#     subject = 'Django ile e-posta gönderimi'
#     message = render_to_string('email_template.html', {'name': 'Django'})
#     sender = 'gonderen@example.com'
#     recipient_list = ['alici@example.com']
#     send_mail(subject, message, sender, recipient_list, html_message=message)
#     return render(request, 'email_sent.html')
from django.utils.translation import activate, gettext_lazy as _
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.conf import settings

def set_language(request):
    lang_code = request.GET.get('language')
    if lang_code:
        activate(lang_code)
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        messages.success(request, _('Language set to %(language)s.') % {'language': dict(settings.LANGUAGES)[lang_code]})
        return response
    else:
        return HttpResponseBadRequest(_('Language code is required.'))


