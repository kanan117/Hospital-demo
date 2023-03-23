from django import forms
from core.models import Contact
from django import forms
# from core.models import Subscriber

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'pattern': '[A-Za-z]+',
                'title': 'Only alphabetical characters are allowed.'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Message'
            })
        }

# class SubscribeForm(forms.Form):
#      class Meta:
#         model = Subscriber
#         fields = ['email']
#         widgets = {
#                 'email': forms.EmailInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Email'
#             }),}
#         emaill = forms.EmailField(required=True)
