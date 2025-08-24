from django.db import models
from users.models import Profile  # из папки users импортируем класс Profile (профиль разработчика)


# coздаем таблицу Проекты
class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)  # добавили новое поле профиль пользователя
    title = models.CharField(max_length=200)  # название статьи (поле обязат. для заполнения)
    description = models.TextField(null=True, blank=True)  # описание статьи со значением Null поле необяз. для заполн.
    featured_images = models.ImageField(upload_to="projects/%Y/%m/%d/", blank=True, default="default.jpg")  # картинка с изображением сохр. в базе в папке project/год/месяц/день
    demo_link = models.CharField(max_length=2000, blank=True)  # поле ссылки (необязат. для заполн.)
    source_link = models.CharField(max_length=2000, blank=True)  # поле ссылки (необязат. для заполн.)
    tags = models.ManyToManyField('Tag', blank=True)  # связь с другой таблицей (Tag) многие ко многим
    vote_total = models.IntegerField(default=0, blank=True)  # количество человек котор. проголосовало за проект
    vote_rating = models.IntegerField(default=0, blank=True)  # количество положит. отзывов
    created = models.DateTimeField(auto_now_add=True)  # время создания

    def __str__(self):
        return self.title


# создаем новую таблицу(связь с основной таблицей)
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

# строковое представление обьекта
    def __str__(self):
        return self.name
