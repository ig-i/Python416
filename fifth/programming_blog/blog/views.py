from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy  # перенаправление после отправки данных на какую то страницу
from django.contrib.auth.mixins import LoginRequiredMixin  # закрыть доступ незарегестрированным пользователям)
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


from .forms import *   # импорт форму

from .models import *

from .utils import *


# menu = [
#     {'title': "Добавить статью", 'url_name': "add_page"},  # подготовили меню для вывода на страницу
#     {'title': "Войти", "url_name": 'index'}  # потом перенесли в Utils
# ]


# без модели классы не работают
# при попадании на главную страницу будет вызываться данный класс с HTML страницей
class BlogHome(DataMixin, ListView):  # строго зарезервированные свойства (наследуемся от класса ListVew)
    model = Blog
    template_name = "blog/index.html"
    context_object_name = "posts"  # так выглядит на странице html

    def get_context_data(self, *, object_list=None, **kwargs): # готовый метод для передачи доп. аргументов (переменных)
        context = super().get_context_data(**kwargs)  # контекст для шаблона
        c_def = self.get_user_context(title="Главная страница")  # доп. переменная для шаблона
        return dict(list(context.items()) + list(c_def.items()))  # одинаковые строки у классов

    def get_queryset(self):
        return Blog.objects.filter(is_published=True). select_related("cat")


class ShowPost(DataMixin, DetailView):
    model = Blog
    template_name = "blog/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs): # готовый метод для передачи доп. аргументов (переменных)
        context = super().get_context_data(**kwargs)  # контекст для шаблона
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))  # одинаковые строки у классов


class BlogCategory(DataMixin, ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = "posts"  # так выглядит на странице html

    def get_queryset(self):  # будут отсортировываться только те данные котор. относятся к выбранной категории
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True). select_related("cat")

    def get_context_data(self, *, object_list=None,
                         **kwargs):  # готовый метод для передачи доп. аргументов (переменных)
        context = super().get_context_data(**kwargs)  # контекст для шаблона
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title="Категория - " + str(c.name), cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))  # одинаковые строки у классов


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm  # название новой формы
    template_name = 'blog/addpage.html'
    success_url = reverse_lazy('index')  # на какую страницу мы переходим после заполнения формы
    login_url = reverse_lazy('index')  # незарегестрированного пользователя направляем на главную страницу(закрыт дост.)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items())) # одинаковые строки у классов



