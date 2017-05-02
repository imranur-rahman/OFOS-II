from django.contrib.auth.models import User
from django import forms
from .models import Customer


class UserLoginForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(min_length=6, label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'required': 'true', 'class': "form-control"}))
    username = forms.CharField(label='', min_length=4,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username', 'required': 'true', 'class': "form-control",
                                          'autofocus': 'true'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=6, label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'required': 'true', 'class': "form-control"}))
    dummy_password = forms.CharField(min_length=6, label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Repeat Password', 'required': 'true', 'class': "form-control"}))
    username = forms.CharField(label='', min_length=4,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username', 'required': 'true', 'class': "form-control",
                                          'autofocus': 'true'}))
    email = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Email', 'required': 'true', 'class': "form-control"}))
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'First Name', 'required': 'true', 'class': "form-control"}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Last Name', 'required': 'true', 'class': "form-control"}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'dummy_password']