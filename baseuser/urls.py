from django.urls import path , include
from django.contrib.auth import views as auth_views
from baseuser.views import register, CustomLoginView, login_view 
from . import views
from django.conf.urls import handler403
from django.conf import settings
# from django.contrib.auth.views import logout

urlpatterns = [
  
  path('login/', login_view, name='login'),
  path('register/', register, name='register'),
  # path('profile/', profile, name='profile'),
  path('logout/',auth_views.LogoutView.as_view(next_page='home'), name='logout'),
  # path('', include('social_django.urls', namespace='social')),
  # path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},name='logout'),

]
