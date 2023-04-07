from django.utils.translation import gettext as _
from django import forms
from raport.models import AnalizRaport
from .validate import validate_file_extension


class AnalizRaportForm(forms.ModelForm):
  name_surname = forms.CharField(widget=forms.TextInput(
    attrs={
      'class': 'form-control',
      'placeholder': 'Name Surname'
    }))
  aciklama = forms.CharField(widget=forms.Textarea(
    attrs={
      'class': 'form-control',
      'placeholder': 'Description',
      'rows': '3'
    }))
  dosya = forms.FileField(
    widget=forms.ClearableFileInput(attrs={
      'multiple': True,
      'class': 'form-control-file'
    }),
    validators=[validate_file_extension])

  class Meta:
    model = AnalizRaport
    fields = ('name_surname', 'aciklama', 'dosya')