from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseUser(AbstractUser):
  location = models.CharField(max_length=50)
  updated_at = models.DateTimeField(auto_now=True)
  date_of_birth = models.DateField(blank=True, null=True)
  phone_number = models.CharField(max_length=20, blank=True)
  email = models.EmailField(max_length=255, unique=True)


# class Profile(models.Model):
#     user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='profile')
#     bio = models.TextField(max_length=500, blank=True)
#     website = models.URLField(blank=True)
#     phone_number = PhoneNumberField(max_length=20,blank=True)
#     first_name = models.CharField(max_length=20, blank=True)
#     last_name = models.CharField(max_length=20, blank=True)
