from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)  # заголовок страницы
    description = models.TextField()  # текстовое содержание
    date = models.DateField()  # дата

    def __str__(self):
        return self.title

