from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Rating,Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='valid email address.')
    class meta:
        model = User
        fields = ('username','email','password1','password2',)

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('design', 'usability', 'content',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('photo', 'title', 'url', 'description',)