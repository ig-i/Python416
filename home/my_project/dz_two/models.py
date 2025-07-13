from django.db import models


class Dz2(models.Model):
    title = models.CharField(max_length=200)  # название страницы
    description = models.TextField()  # многострочное текстовое поле
    date = models.DateField()  # тип данных для работы с датой

    def __str__(self):
        return self.title
