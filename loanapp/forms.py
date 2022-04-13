from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import CreateUser


class CreateUserForm(UserCreationForm):
    password2 = forms.CharField(label="Re-enter Password",widget=forms.PasswordInput)

    class Meta:
        model = CreateUser
        fields = ['name', 'address', 'dob', 'gender', 'mobile', 'email']
        labels = {'email': 'Email'}
