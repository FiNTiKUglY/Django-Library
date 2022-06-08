import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(), max_length=30)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(), max_length=30)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(), max_length=30)

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
    name = forms.CharField(label='Имя', widget=forms.TextInput(), required=True, min_length=1, max_length=50)
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(), required=True, min_length=1, max_length=50)
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(), required=True, min_length=13, max_length=13)
    email = forms.EmailField(label='Эл. почта', widget=forms.EmailInput())
    adress = forms.CharField(label='Адрес', widget=forms.TextInput(), required=True, min_length=4, max_length=50)
    index = forms.IntegerField(label='Почтовый индекс', widget=forms.NumberInput(), min_value=100000, max_value=999999)

    class Meta:
        fields = [
            'name',
            'surname',
            'phone',
            'email',
            'adress',
            'index'
        ]

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if re.match(r'[+][0-9]{12}', phone):
            return phone
        raise forms.ValidationError("Неправильный формат телефона")

