from core.models import Setting
from django.shortcuts import render
from baseuser.models import BaseUser
from core.models import Doctors

def settings(request):
    return{
        'setting' : Setting.objects.all()
    }


def doctor_count(request):
    return {'doctor_count': Doctors.objects.count()
            }


def user_count(request):
    return {
        'user_count': BaseUser.objects.count()
        }

