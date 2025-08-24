from django .forms import ModelForm  # импортируем форму связанную с моделью
from .models import Todo  # импортируем модель


# создаем дополнительную форму "Создание задачи"
class TodoForm(ModelForm):
    class Meta:  # зарезервированный класс
        model = Todo
        fields = ['title', 'memo', 'important']  # указываем поля которые будут в новой форме
