from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *

from .models import *

from .utils import *


# menu = [
#     {'title': "Добавить статью", 'url_name': "index"},  # подготовили меню для вывода на страницу
#     {'title': "Войти", "url_name": 'index'}
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
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Blog.objects.filter(is_published=True). select_related("cat")


class ShowPost(DataMixin, DetailView):
    model = Blog
    template_name = "blog/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs): # готовый метод для передачи доп. аргументов (переменных)
        context = super().get_context_data(**kwargs)  # контекст для шаблона
        context['title'] = context['post']  #
        context['menu'] = menu
        return context


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
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpage.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))



