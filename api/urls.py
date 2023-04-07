from django.urls import path
from .views import ContactViewSet, ContactDetailViewSet


urlpatterns = [
    path('Contact/', ContactViewSet.as_view()),

]

