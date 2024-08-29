from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 mt-2 border-2 border-gray-400 rounded-md text-black',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 mt-2 border-2 border-gray-400 rounded-md text-black',
            'placeholder': 'Password'
        })
    )