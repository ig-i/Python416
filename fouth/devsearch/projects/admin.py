from django.contrib import admin

from .models import Project, Tag

# регистрируем таблицы в проекте
admin.site.register(Project)
admin.site.register(Tag)
