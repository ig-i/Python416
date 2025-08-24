from django.db import models


class Mobile(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField('mobile/images/')
    url = models.URLField(blank=True)  # поле необязательное для заполнения

    def __str__(self):
        return self.title
