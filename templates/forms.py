from django.db import transaction
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

######################## Creating a user

class UserForm(UserCreationForm):
    email = forms.EmailField()

    password1 = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label= ("Confirm Password"),
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1' ,'password2' )
        help_texts = {
            'username': None,
            'email': None,
            'password1' : None,
            'password2' : None,
        }

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = [
            "username",
            "fname",
            "lname",
            "email",
            "pfp"
        ]