from django.urls import path
# from core.views import base
from core import views

from core.views import (home, about, appointment, base, blog, 
                        booking_list, contact, doctor_details, doctor, doctors,
                        error, faq, index_2, login, service_details, service,
                        services, blog_details)

urlpatterns = [
  path('', home, name='home'),
  path('', views.about, name='about'),
  path('appointment/', appointment, name='appointment'),
  path('base/', base, name='base'),
  # path('', views.blogs, name='blog'),
  # path('blogs/<int:pk>/', blogs, name= 'blogs'),
  path('blogs/', blog, name='blog'),
  path('blogs/<int:id>', views.blog_details, name='blogdetails'),
  path('booking-list/', booking_list, name='booking_list'),
  path('contact/', contact, name='contact'),
  path('doctor-details/', doctor_details, name='doctor_details'),
  path('doctor/', doctor, name='doctor'),
  path('doctors/', doctors, name='doctors'),
  path('error/', error, name='error'),
  path('faq/', faq, name='faq'),
  path('index-2/', index_2, name='index_2'),
  path('login/', login, name='login'),
  path('service-details/', service_details, name='service_details'),
  path('service/', service, name='service'),
  path('services/', services, name='services'),
  path('blog-details/', blog_details, name='blog-details' )
]
