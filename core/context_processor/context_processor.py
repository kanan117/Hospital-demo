from core.models import Setting

def settings(request):
    return{
        'setting' : Setting.objects.all()
    }
