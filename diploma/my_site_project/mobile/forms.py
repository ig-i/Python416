from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):  # переопределили стандартную форму регистрации
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RegisterForm(forms.Form):  # форма обратной связи ( не связанная с моделью)
    name = forms.CharField(label="Введите имя", max_length=255)
    telephone = forms.CharField(label="Введите телефон", max_length=255)
    email = forms.EmailField(label="Email")
    title = forms.CharField(label="Введите марку авто", max_length=255)
    text = forms.CharField(label="Введите цвет авто", max_length=255)
    year = forms.CharField(label="Введите год выпуска", max_length=255)

    # name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    # telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите телефон'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введите почту'}))
    # title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите марку авто'}))
    # text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите цвет авто'}))
    # year = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите год выпуска'}))
    #
    # class Meta:
    #     model = User
    #     fields = ['name', 'telephone', 'email', 'title', 'text', 'year']
