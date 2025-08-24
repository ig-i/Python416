from django.db import models
from django.contrib.auth.models import User  # класс из таблицы auth


# создание таблицы
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)  # поле необязательное для заполнения (без NULL)
    created = models.DateTimeField(auto_now_add=True)  # дата создания нашей задачи с автом. заполнением
    date_completed = models.DateTimeField(blank=True, null=True)  # в ячейке будет стоять NULL
    important = models.BooleanField(default=False)  # поле задачи (важная - неважная)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # делаем связь

# возвращаем строковое представление обьекта (после создания модели регистрируем в админ.ру)
    def __str__(self):
        return self.title
