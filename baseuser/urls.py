from django.urls import path
from django.contrib.auth import views as auth_views
from baseuser.views import register, CustomLoginView, login_view ,profile
from . import views
from django.conf.urls import handler403

handler403 = 'myapp.views.my_custom_permission_denied_view'
urlpatterns = [
  
  path('login/', login_view, name='login'),
  path('register/', register, name='register'),
  path('profile/', views.profile, name='profile'),
  path('logout/',auth_views.LogoutView.as_view(next_page='home'), name='logout'),
  
]
