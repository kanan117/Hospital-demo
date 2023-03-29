
from core.views import base
from core import views
from django.urls import path
from . import views
from django.conf.urls import handler403
# from .views import set_language
from django.urls import path

handler403 = 'myapp.views.my_custom_permission_denied_view'
from core.views import (home, about, appointment, base,  booking_list,
                        contact, doctor_details, doctor, doctors, error, faq,
                        index_2, service_details, service, services,
                        blog_details,BlogsListView)

urlpatterns = [
    
  path('', home, name='home'),
  path('about/', about, name='about'),
  path('appointment/', appointment, name='appointment'),
  path('base/', base, name='base'),
  path('blogs/', BlogsListView.as_view(), name='blog'),
  # path('blogs/', blog, name='blog'),
  path('blogs/<int:id>', views.blog_details, name='blogdetails'),
  path('booking_list/', booking_list, name='booking_list'),
  path('contact/', contact, name='contact'),
  path('doctor_details/', doctor_details, name='doctor_details'),
  path('doctor/', doctor, name='doctor'),
  path('doctors/', doctors, name='doctors'),
  path('error/', error, name='error'),
  path('faq/', faq, name='faq'),
  path('index-2/', index_2, name='index_2'),
  path('service-details/', service_details, name='service_details'),
  path('service/', service, name='service'),
  path('services/', services, name='services'),
  path('blog_details/', blog_details, name='blog_details'),
  
  
]