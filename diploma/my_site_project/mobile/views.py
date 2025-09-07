from django.contrib.auth.forms import UserCreationForm  # импортируем стандартную форму
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from mobile.models import Mobile


def signup_user(request):
    if request.method == "GET":
        return render(request, 'mobile/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == ['password2']:  # создать нового  пользователя
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()  # сохраняем нового пользователя
            login(request, user)
            return redirect('index')  # перенаправляем пользователя на эту страницу


def index(request):
    projects = Mobile.objects.all()
    return render(request, 'mobile/index.html', {'projects': projects})
