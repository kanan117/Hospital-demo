from core.models import Setting

def settings(request):
    return{
        'setting' : Setting.objects.all()
    }

from core.models import Doctors

def doctor_count(request):
    return {'doctor_count': Doctors.objects.count()}
