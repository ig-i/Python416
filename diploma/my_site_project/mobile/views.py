from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from mobile.models import Mobile

from .forms import *  # импортируем форму


# регистрация и автоматическая авторизация
def signup_user(request):
    if request.method == "GET":
        return render(request, 'mobile/signupuser.html', {'form': RegisterUserForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:  # создать нового  пользователя
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()  # сохраняем нового пользователя
                login(request, user)
                return redirect('index')  # перенаправляем пользователя на главную страницу
            except IntegrityError:
                return render(request, 'mobile/signupuser.html',
                              {'form': RegisterUserForm(),
                               'error': 'Такое имя пользователя уже существует. Задайте другое'})

        else:
            return render(request, 'mobile/signupuser.html',
                          {'form': RegisterUserForm(), 'error': 'Пароли не совпадают'})


def index(request):
    projects = Mobile.objects.all()
    return render(request, 'mobile/index.html', {'projects': projects})


def detail(request, pk):
    detail_obj = Mobile.objects.get(id=pk)
    # print(detail_obj)
    return render(request, 'mobile/details.html', {'detail': detail_obj})


def company(request):
    projects = Mobile.objects.all()
    return render(request, 'mobile/company.html', {'projects': projects})


def contact(request):
    projects = Mobile.objects.all()
    return render(request, 'mobile/contact.html', {'projects': projects})


def zakaz(request, pk):
    zakaz_obj = Mobile.objects.get(id=pk)
    print(zakaz_obj)
    return render(request, 'mobile/zakaz.html', {'zakaz': zakaz_obj, 'form': RegisterForm()})


def register(request):
    if request.method == "POST":
        return render(request, 'mobile/zakaz.html', {'form': RegisterForm()})
    else:
        return render(request, 'mobile/zakaz.html', {'form': RegisterForm()})


# def contact_form(request, form):
#     if request.method == "GET":
#         return render(request, 'mobile/zakaz.html', {'form': ContactForm()})
    # print(form.cleaned_data)
    # subject = "Message"
    # body = {
    #     'name': form.cleaned_data['name'],
    #     'telephone': form.cleaned_data['telephone'],
    #     'email': form.cleaned_data['email'],
    #     'title': form.cleaned_data['title'],
    #     'text': form.cleaned_data['text'],
    #     'year': form.cleaned_data['year'],
    # }
    # message = "\n".join(body.values())
    # try:
    #     send_mail(
    #         subject, message, form.cleaned_data['email'], ['admin@localhost']
    #     )
    # except BadHeaderError:
    #     return HttpResponse("Данные не отправлены")
    #
    # return redirect('index')
