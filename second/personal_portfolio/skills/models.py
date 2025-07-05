from django.db import models

from django.db import models


class Skills(models.Model):  # создание таблицы
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField('skills/images/')
    url = models.URLField(blank=True)
