from django.shortcuts import render
from django.views.generic import ListView  # список элементов

from .models import *

menu = [
    {'title': "Добавить статью", 'url_name': "index"},  # подготовили меню для вывода на страницу
    {'title': "Войти", "url_name": 'index'}
]


# без модели классы не работают
# при попадании на главную страницу будет вызываться данный класс с HTML страницей
class BlogHome(ListView):  # строго зарезервированные свойства
    model = Blog
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs): # готовый метод для передачи доп. аргументов (переменных)
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"  # доп. переменная для шаблона
        context['menu'] = menu
        return context

