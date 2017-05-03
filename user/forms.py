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

    def clean(self):
        cleaned_data = self.cleaned_data

        if self._errors:
            self.data['password'] = 'abc'
            raise forms.ValidationError("Wrong username password combination!")
        else:
            return cleaned_data


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=6, label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'required': 'true', 'class': "form-control"}))
    dummy_password = forms.CharField(min_length=6, label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Repeat Password', 'required': 'true', 'class': "form-control"}))
    username = forms.CharField(label='', min_length=4,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username', 'required': 'true', 'class': "form-control",
                                          'autofocus': 'false'}))
    email = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Email', 'required': 'true', 'class': "form-control"}))
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'First Name', 'required': 'true', 'class': "form-control",
                                            'autofocus': 'true'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Last Name', 'required': 'true', 'class': "form-control"}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'dummy_password']


    '''def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        print(cleaned_data)
        username ='''