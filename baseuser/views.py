from django.shortcuts import render
from baseuser.forms import BaseUserForm
from core.models import Setting
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import Profile

from django.shortcuts import render
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


from django.shortcuts import render

def my_custom_permission_denied_view(request, exception=None):
    return render(request, 'error.html', {})


def register(request):
  form = BaseUserForm()
  if request.method == 'POST':
    form = BaseUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      # login the user after successful registration
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect('home')
  context = {
    'setting': Setting.objects.first(),
    'title': "Register",
    'form': form,
  }
  return render(request, "register.html", context)


def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')
  else:
    form = LoginForm()
  return render(request, 'login.html', {'form': form})


from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
  template_name = 'login.html'

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                          request.FILES,
                                          instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'profile.html', context)


