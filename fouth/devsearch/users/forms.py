from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# переопределяем стандартную форму для формы регистрации пользователя
class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields in self.fields.values():  # корректируем поля (расширили) формы в цикле через init
            fields.widget.attrs.update({'class': 'input'})

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']  # добавляем доп. поля в форму регистрац.
        labels = {'first_name': 'Name'}   # свойство котор. позволяет переименовать поле в форме
