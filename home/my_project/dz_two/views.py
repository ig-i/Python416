from django.shortcuts import render, get_object_or_404, redirect
from .models import Dz2
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # встр. класс в jango котор имеет свою форму
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate  # встроенная функция авторизации и регистр. данных пользов.
from django .db import IntegrityError


def home(request):
    return render(request, 'dz_two/home.html')


def dz_two(request):
    dz_two = Dz2.objects.order_by('date')  # получаем данные из базы данных по дате
    return render(request, 'dz_two/dz_two.html', {'dz_two': dz_two})


def detail(request, dz_id):
    dz = get_object_or_404(Dz2, pk=dz_id)
    return render(request, 'dz_two/detailes.html', {'dz_two': dz})


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'dz_two/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:  # проверяем вводимые пароли
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()                             # сохраняем обьект user в базу данных
                login(request, user)                    # авторизация пользователя
                return redirect('currenttodos')         # перенаправляем пользователя после авторизации на другой URL
            except IntegrityError:
                return render(request, 'dz_two/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя уже существует. Задайте другое'})

        else:
            return render(request, 'dz_two/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def current_todos(request):
    return render(request, 'dz_two/currenttodos.html')


def logout_user(request):    # выход из учетной записи (ВЫЙТИ)
    if request.method == "POST":
        logout(request)
        return redirect('home')


def login_user(request):
    if request.method == "GET":
        return render(request, 'dz_two/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'dz_two/loginuser.html', {
                'form': AuthenticationForm(),
                'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('currenttodos')
