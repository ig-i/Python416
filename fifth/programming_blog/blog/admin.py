from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}   # вывод поля title в поле slug админики и на странице веб
    list_display = ('id', 'title', 'cat', 'time_created', 'photo', 'is_published') # вывод доп.полей в админке и модели
    list_display_links = ('id', 'title')  # делаем ссылками названия полей в админке
    search_fields = ('title', 'content')  # делаем окно поиска в админке по эти полям
    list_editable = ('is_published',) #  атрибут, который задает возм. править поля непосредственно на странице списка записей, не переходя на страницу продукта
    list_filter = ('is_published', 'time_created',) # фильтр списка


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')  # вывод доп.полей в админке и модели
    list_display_links = ('id', 'name')  # делаем ссылками названия полей в админке
    search_fields = ('name',)  # делаем окно поиска в админке по эти полям


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

