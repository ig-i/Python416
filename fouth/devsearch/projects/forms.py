# форма связанная с моделью
from django.forms import ModelForm
from .models import Project
from django import forms


# создаем форму для заполнения со стороны сайта
class ProjectForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields in self.fields.values():  # корректируем поля (расширили) формы в цикле через init
            fields.widget.attrs.update({'class': 'input'})

    class Meta:  # служебный класс c 2 обязательными полями

        model = Project
        fields = ['title', 'featured_images', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {'tags': forms.CheckboxSelectMultiple()}  # возможность выбора чекбоксами поля Tags формы
