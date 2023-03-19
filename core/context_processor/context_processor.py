from core.models import Setting

def setting(request):
    return{
        'setting' : Setting.objects.all()
    }
