from django.urls import path
from .views import ContactViewSet, ContactDetailViewSet ,SubscriberAPIview


urlpatterns = [
    path('Contact/', ContactViewSet.as_view()),
    path('subscriber/' ,SubscriberAPIview.as_view(), name= 'subscriber')

]

