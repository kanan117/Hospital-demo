from django.shortcuts import render, get_object_or_404, redirect
from raport.models import AnalizRaport
from raport.forms import AnalizRaportForm
import random
import os
from django.contrib.auth.decorators import user_passes_test

def rapor_detay(request, rapor_id):
    rapor = get_object_or_404(AnalizRaport, id=rapor_id)
    context = {'rapor': rapor}
    return render(request, 'rapor_detay.html', context)



def rapor_search(request):
    if 'analiz_id' in request.GET and request.GET['analiz_id']:
        try:
            analiz_id = int(request.GET['analiz_id'])
            rapor = AnalizRaport.objects.get(id=analiz_id)
            return redirect('rapor_detay', rapor_id=rapor.id)
        except (ValueError, AnalizRaport.DoesNotExist):
            error_message = "Invalid report ID"
            return render(request, 'rapor_search.html', {'error_message': error_message})
    return render(request, 'rapor_search.html')


@user_passes_test(lambda u: u.has_perm('raport.can_add_raport'))
def rapor_add(request):
    if request.method == "POST":
        form = AnalizRaportForm(request.POST, request.FILES)
        if form.is_valid():
            rapor = form.save(commit=False)
            rapor.id = random.randint(100000, 999999)

            # Dosya ismini rapor id ile aynı yap
            dosya_adi, dosya_uzantisi = os.path.splitext(rapor.dosya.name)
            rapor.dosya.name = f"{rapor.id}{dosya_uzantisi}"
            rapor.save()

            return redirect('rapor_detay', rapor_id=rapor.id)
    else:
        form = AnalizRaportForm()
    return render(request, 'rapor_add.html', {'form': form})

