from .models import *
from django.db.models import Count

menu = [
    {'title': "Добавить статью", "url_name": 'add_page'},
    {'title': "Войти", "url_name": 'index'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('blog'))  # сколько элементов в блоге Категории заполнены тогда они вывод

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:  # если текущий пользватель не авторизирован то передаем меню
            user_menu.pop(0)                       # без 0 индекса (без - добавить статью)

        context['menu'] = user_menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
