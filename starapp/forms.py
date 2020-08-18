from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='valid email address.')
    class meta:
        model = User
        fields = ('username','email','password1','password2',)
