from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone_number', 'first_name', 'last_name', 'sex', 'country', 'address', 'bio', 'qualifications', 'job_title']
