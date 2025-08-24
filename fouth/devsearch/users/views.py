from django.shortcuts import render, redirect
from .models import Profile  # импортируем модель Профиль пользователя
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # это встроенная система сообщений в django
from django.contrib.auth.forms import UserCreationForm  # встр. класс где хранится форма регистрации пользователей
from .forms import CustomUserCreationForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username'].lower()  # при авторизации данный преобразов. в нижн. регистр
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Username does not exist')  # вывод сообщения пользователю ошибка

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or password is incorrect")  # вывод сообщения пользователю ошибка

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, "User was logged out!")  # сообщение что пользователь разлогинен
    return redirect('login')


def profiles(request):  # функция для вывода на страницу html документа
    prof = Profile.objects.all()
    contex = {
        'profiles': prof
    }
    return render(request, 'users/index.html', contex)


def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)

    top_skills = prof.skill_set.exclude(description__exact="")  # получаем доступ к таблице Skill поле description
    other_skills = prof.skill_set.filter(description="")
    contex = {
        'profile': prof,
        'top_skills': top_skills,
        'other_skills': other_skills,
    }

    return render(request, 'users/profile.html', contex)


def register_user(request):  # функция регистрации нового пользователя на странице
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error has occurred during registration')

    contex = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_register.html', contex)


# защита от незарегестрированного пользователя
@login_required(login_url='login')
def user_account(request):
    prof = request.user.profile  # получаем доступ у текущего (авторизированного) пользователя к его профилю
    skills = prof.skill_set.all()  # получаем доступ к таблице skill через переменную prof и берем все данные
    projects = prof.project_set.all()  # получили доступ к табл. Project из модели через перемен. prof и берем все данные

    context = {
        'profile': prof,
        'skills': skills,
        'projects': projects
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    return render(request, 'users/profile_form.html')
