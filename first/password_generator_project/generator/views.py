from django.http import HttpResponse
from django.shortcuts import render
import random


def home(request):
    lst = list(range(6, 15))
    return render(request, "generator/home.html", {'lst': lst})  # подключаем html страницу


def password(request):
    char = [chr(i) for i in range(97, 123)]  # генерируем коды символов в нижнем регистре в указанном интервале
    # print(char)
    if request.GET.get('uppercase'):         # генерируем коды символов в верхнем регистре в заданном интервале
        char.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('numbers'):                     # генерируем числовые коды символов
        char.extend([chr(i) for i in range(48, 58)])

    if request.GET.get('special'):                     # генерируем спецсимволы
        char.extend([chr(i) for i in range(33, 48)])

    length = int(request.GET.get("length"))             # получаем данные из home.html name='length' (кол-во символов)

    psw = ''
    for i in range(length):
        psw += random.choice(char)                          # возвращает случайную последовательность элементов
    return render(request, 'generator/password.html', {'password': psw})


def norms(request):
    # nrw = list(range(6, 15))
    return render(request, "generator/norms.html")
