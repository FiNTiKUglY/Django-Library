from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]


class LogInForm(AuthenticationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class MailForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput())
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput())
    adress = forms.CharField(label='Адрес', widget=forms.TextInput())
    index = forms.IntegerField(label='Почтовый индекс', widget=forms.TextInput())
