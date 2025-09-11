from django.contrib.auth.forms import UserCreationForm  # импортируем стандартную форму
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from mobile.models import Mobile


def signup_user(request):
    if request.method == "GET":
        return render(request, 'mobile/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:  # создать нового  пользователя
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()  # сохраняем нового пользователя
                login(request, user)
                return redirect('index')  # перенаправляем пользователя на главную страницу
            except IntegrityError:
                return render(request, 'mobile/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя уже существует. Задайте другое'})

        else:
            return render(request, 'mobile/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def index(request):
    projects = Mobile.objects.all()
    return render(request, 'mobile/index.html', {'projects': projects})


def detail(request, mobile_id):
    mobile = get_object_or_404(Mobile, pk=mobile_id)
    return render(request, 'mobile/details.html', {'mobile': mobile})


