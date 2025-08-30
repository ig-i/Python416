from django.db import models
from django.contrib.auth.models import User  # класс из таблицы auth


# создание таблицы
class Mobile(models.Model):
    title = models.CharField(max_length=200)  # название страницы
    description = models.TextField()  # многострочное текстовое поле
    date = models.DateField()  # тип данных для работы с датой
    image = models.ImageField(upload_to='mobile/images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # делаем связь
    demo_link = models.CharField(max_length=2000, blank=True)  # поле ссылки (необязат. для заполн.)
    created = models.DateTimeField(auto_now_add=True)  # время создания
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(blank=True)

# возвращаем строковое представление обьекта (после создания модели регистрируем в админ.ру)
    def __str__(self):
        return self.title

