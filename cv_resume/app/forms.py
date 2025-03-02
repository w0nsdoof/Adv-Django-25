from django import forms 

from .models import Contact, CV


class CVForm(forms.ModelForm): 
    class Meta: 
        model = CV 
        fields = ['name', 'email', 'profile_picture'] 

class ContactForm(forms.ModelForm): 
    class Meta: 
        model = Contact 
        fields = ['name', 'email', 'message'] 
        
        from django import forms 