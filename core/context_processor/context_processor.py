from core.models import Setting

def settings(request):
    return{
        'settings' : Setting.objects.all()
    }

