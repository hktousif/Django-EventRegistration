from django import forms
from .models import *
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfileModel
        fields = ('Contact_No', 'DOB', 'Profile_Picture')
        widgets = {
            'DOB': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'Contact_No': forms.TextInput(attrs={'placeholder': 'Enter Contact No', 'type': 'tel'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
