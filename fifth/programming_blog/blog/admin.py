from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.safestring import mark_safe  # отображение данных html разметки в admin панели


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        models = Blog
        fields = "__all__"


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    prepopulated_fields = {"slug": ("title",)}   # вывод поля title в поле slug админики и на странице веб
    list_display = ('id', 'title', 'cat', 'time_created', 'get_html_photo', 'is_published') # вывод доп.полей в админке и модели
    list_display_links = ('id', 'title')  # делаем ссылками названия полей в админке
    search_fields = ('title', 'content')  # делаем окно поиска в админке по эти полям
    list_editable = ('is_published',) #  атрибут, который задает возм. править поля непосредственно на странице списка записей, не переходя на страницу продукта
    list_filter = ('is_published', 'time_created')  # фильтр списка
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo_inner', 'is_published', 'time_created', 'time_update',)  # какие поля хотим вывести в админке (предпросмотр)
    readonly_fields = ('get_html_photo_inner', 'time_created','time_update',)  # не редактируемое поле отдельно прописываем
    save_on_top = True  # можно продублировать нижнюю панель админки на верху

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width ='70'>") # выводим картинки в админку (предпросмотр))

    def get_html_photo_inner(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width ='200'>")  # выводим картинки в админку в поле

    get_html_photo.short_description = "Миниатюра" # краткое описание для любого поля (short_description)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')  # вывод доп.полей в админке и модели
    list_display_links = ('id', 'name')  # делаем ссылками названия полей в админке
    search_fields = ('name',)  # делаем окно поиска в админке по эти полям


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)


admin.site.site_title = 'Админ-панель блога'
admin.site.site_header = 'Админ-панель блога'

