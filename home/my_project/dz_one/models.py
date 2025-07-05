from django.db import models


class Dz(models.Model):  # создали поля в таблице с графами в базе
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField('dz_one/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
