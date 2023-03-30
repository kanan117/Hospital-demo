from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms.widgets import SelectDateWidget
from phonenumber_field.modelfields import PhoneNumberField
from .models import BaseUser


#registration form
class BaseUserForm(UserCreationForm):
  email = forms.EmailField(max_length=35,
                           help_text='Required. Enter a valid email address.',
                           widget=forms.EmailInput(attrs={
                             'class': 'form-control',
                             'placeholder': 'Email'
                           }))

  first_name = forms.CharField(
    max_length=30,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'pattern': '[A-Za-z]+',
        'title': 'Only alphabetical characters are allowed.'
      }))

  last_name = forms.CharField(
    max_length=30,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'pattern': '[A-Za-z]+',
        'title': 'Only alphabetical characters are allowed.'
      }))

  date_of_birth = forms.DateField(
    required=True, widget=SelectDateWidget(years=range(1955, 2023)))

  password1 = forms.CharField(
    strip=False,
    widget=forms.PasswordInput(attrs={
      'class': 'form-control',
      'placeholder': 'Password'
    }),
  )
  #help_text='Your password must contain at least 8 characters, at least one digit, and can\'t be entirely alphabetical or entirely numeric.')

  password2 = forms.CharField(
    strip=False,
    widget=forms.PasswordInput(attrs={
      'class': 'form-control',
      'placeholder': 'Confirm Password'
    }),
    help_text='Enter the same password as before, for verification.')

  class Meta:
    model = BaseUser
    fields = [
      'username',
      'email',
      'first_name',
      'last_name',
      'password1',
      'password2',
      'date_of_birth',
    ]
    widgets = {
      'username':
      forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
      }),
    }

  def clean_password1(self):
    password1 = self.cleaned_data.get('password1')
    if len(password1) < 8:
      raise forms.ValidationError(
        "Your password must contain at least 8 characters.")
    elif any(char.isdigit() for char in password1) == False:
      raise forms.ValidationError(
        "Your password must contain at least one digit.")
    elif password1.isalpha():
      raise forms.ValidationError(
        "Your password can't be entirely alphabetical.")
    elif password1.isnumeric():
      raise forms.ValidationError("Your password can't be entirely numeric.")
    elif not password1[0].isupper():
      raise forms.ValidationError(
        "Your password must start with a capital letter.")
    return password1


#login form
class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(
    attrs={
      'class': 'form-control',
      'placeholder': 'Username'
    }))
  password = forms.CharField(widget=forms.PasswordInput(
    attrs={
      'class': 'form-control',
      'placeholder': 'Password'
    }))


#update user area

# class UserUpdateForm(forms.ModelForm):
#   email = forms.EmailField(widget=forms.EmailInput(attrs={
#     'class': 'form-control',
#     'placeholder': 'Email'
#   }))

#   first_name = forms.CharField(
#     max_length=20,
#     widget=forms.TextInput(
#       attrs={
#         'class': 'form-control',
#         'placeholder': 'First Name',
#         'pattern': '[A-Za-z]+',
#         'title': 'Only alphabetical characters are allowed.'
#       }))

#   last_name = forms.CharField(
#     max_length=20,
#     widget=forms.TextInput(
#       attrs={
#         'class': 'form-control',
#         'placeholder': 'Last Name',
#         'pattern': '[A-Za-z]+',
#         'title': 'Only alphabetical characters are allowed.'
#       }))

#   phone_number = forms.CharField(
#     max_length=13,
#     widget=forms.TextInput(
#       attrs={
#         'class': 'form-control',
#         'placeholder': 'Phone Number',
#         'pattern': '\d*',
#         'title': 'Enter a valid phone number with only numeric digits, up to 13 characters.'
#       }),
#     required=False)

#   password = forms.CharField(
#     widget=forms.PasswordInput(
#       attrs={
#         'class': 'form-control',
#         'placeholder': 'Password',
#         'title': 'Password must be at least 8 characters long and start with a capital letter.'
#       }),
#     required=False,
#     validators=[
#       validators.MinLengthValidator(8, message="Password must be at least 8 characters long."),
#       validators.RegexValidator(
#         regex=r'[A-Z].*',
#         message="Password must start with a capital letter.",
#       ),
#     ])

#   confirm_password = forms.CharField(
#     widget=forms.PasswordInput(
#       attrs={
#         'class': 'form-control',
#         'placeholder': 'Confirm Password',
#         'title': 'Please confirm your password.',
#       }),
#     required=False)

#   def clean(self):
#     cleaned_data = super().clean()
#     password = cleaned_data.get('password')
#     confirm_password = cleaned_data.get('confirm_password')

#     if password and confirm_password and password != confirm_password:
#       raise forms.ValidationError("Passwords do not match.")

#     return cleaned_data

#   class Meta:
#     model = BaseUser
#     fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'confirm_password']

# class ProfileUpdateForm(forms.ModelForm):
#   class Meta:
#     model = BaseUser
#     fields = []
