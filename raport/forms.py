from django import forms
from .models import AnalizRaport

class AnalizRaportForm(forms.ModelForm):
    name_surname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name Surname'
        }))
    aciklama = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Açıklama',
            'rows': '3',
        }))
    dosya = forms.FileField(widget=forms.ClearableFileInput(
        attrs={
            'multiple': True,
            'class': 'form-control-file'
        }))
    
    class Meta:
        model = AnalizRaport
        fields = ('name_surname', 'aciklama', 'dosya')
