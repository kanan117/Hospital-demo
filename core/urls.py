from django.urls import path
# from core.views import base

from core.views import (home, about, appointment, base, blog_details,
                        booking_list, contact, doctor_details, doctor, doctors,
                        error, faq, index_2, login, service_details, service,
                        services)

urlpatterns = [
  path('', home, name='home'),
  path('about/', about, name='about'),
  path('appointment/', appointment, name='appointment'),
  path('base/', base, name='base'),
  path('blog-details/', blog_details, name='blog_details'),
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
]