from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)  # выводим дополнительное поле  created в админку


# регистрируем модель (таблицу) в admin
admin.site.register(Todo, TodoAdmin)

