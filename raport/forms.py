from django import forms
from .models import AnalizRaport

class AnalizRaportForm(forms.ModelForm):
  class Meta:
    model = AnalizRaport
    fields = ('title', 'aciklama', 'sonuc', 'dosya')


