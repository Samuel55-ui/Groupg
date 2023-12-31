# forms.py
from django import forms
from .models import Profilehr

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profilehr
        fields = ['image', 'phone_number', 'first_name', 'country', 'address', 'bio', 'qualifications']
