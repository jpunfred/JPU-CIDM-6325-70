# advinterface/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Major
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label=_("Email"),
        widget=forms.TextInput(attrs={'autofocus': True}),
    )

    class Meta:
        model = User
        fields = ['username', 'password']


class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    buff_id = forms.CharField(max_length=7)
    major = forms.ChoiceField(choices=[('CIS', 'Computer Information Systems'),
                                       ('CIS_DM', 'CIS Decision Management')],
                              required=True)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'password1', 'password2',
            'buff_id', 'major'
        ]


class StudentLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
