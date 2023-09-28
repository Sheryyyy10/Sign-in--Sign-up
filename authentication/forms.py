from django import forms
from .models import UserProfile

class Contactforms(forms.Form):
    Firstname = forms.CharField()
    Lastname = forms.CharField()
    username = forms.CharField()
    Email = forms.EmailField()
    Password = forms.CharField()
    ConfirmPassword = forms.CharField(label='Confirm Pass')


class UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ['profile_image']

