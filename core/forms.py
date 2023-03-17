from django import forms

from core.models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['email', 'name',  'phone_number',  'message']
        widgets = {
            "name" : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Name'}),
            "email" : forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : "Email"}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Phone Number'}),
           
            "message" : forms.Textarea(attrs={'class' : 'form-control', 'row' : 3, 'placeholder' : 'Message'})
        }