from django import forms
from .models import ServicePageLead

class ServicePageLeadForm(forms.ModelForm):
    class Meta:
        model = ServicePageLead
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 3}),
        }
