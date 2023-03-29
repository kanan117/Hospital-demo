from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from baseuser.forms import BaseUserForm
# from .forms import UserUpdateForm, ProfileUpdateForm
from core.models import Setting
from .forms import LoginForm
from django.views.generic import ListView


def register(request):
    form = BaseUserForm()
    if request.method == 'POST':
        form = BaseUserForm(request.POST)
        if form.is_valid():
            user = form.save()
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
    

class CustomLoginView(LoginView):
    template_name = 'login.html'


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         if user_form.is_valid():
#             user_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')
#     else:
#         user_form = UserUpdateForm(instance=request.user)

#     # context = {
#     #     'user_form': user_form,
#     #     'setting': Setting.objects.first()
#     # }

#     return render(request, 'profile.html')

