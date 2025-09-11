from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView  # список элементов

from .models import *

menu = [
    {'title': "Добавить статью", 'url_name': "index"},  # подготовили меню для вывода на страницу
    {'title': "Войти", "url_name": 'index'}
]


# без модели классы не работают
# при попадании на главную страницу будет вызываться данный класс с HTML страницей
class BlogHome(ListView):  # строго зарезервированные свойства (наследуемся от класса ListVew)
    model = Blog
    template_name = "blog/index.html"
    context_object_name = "posts"  # так выглядит на странице html

    def get_context_data(self, *, object_list=None, **kwargs): # готовый метод для передачи доп. аргументов (переменных)
        context = super().get_context_data(**kwargs)  # контекст для шаблона
        context['title'] = "Главная страница"  # доп. переменная для шаблона
        context['cat_selected'] = 0
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True). select_related("cat")


class ShowPost(DetailView):
    model = Blog
    template_name = "blog/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs): # готовый метод для передачи доп. аргументов (переменных)
        context = super().get_context_data(**kwargs)  # контекст для шаблона
        context['title'] = context['post']  #
        context['menu'] = menu
        return context


class BlogCategory(ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = "posts"  # так выглядит на странице html

