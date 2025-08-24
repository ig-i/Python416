from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'todo/home.html')


def signup_user(request):
    if request.method == "GET":
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя уже существует. Задайте другое'})
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


# Задачи
@login_required
def current_todos(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=True) # по какому условию будем выводить задачи
    return render(request, 'todo/currenttodos.html',
                  {'todos': todos})


@login_required
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def login_user(request):
    if request.method == "GET":
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('currenttodos')


# Создание задачи
@login_required()
def create_todo(request):
    if request.method == "GET":  # получаем данные методом GET
        return render(request, 'todo/createtodo.html', {"form": TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)  # передаем данные методом POST (создание новой записи)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()  # сохраняем все  данные в базу данных
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {
                "form": TodoForm(),
                'error': 'Переданы неверные данные. Попробуйте еще раз'})


# (Актуальные задачи) Выводим любую страницу задач по ссылке
@login_required
def view_todo(request, todo_pk):  # первичный ключ который придет в адресную строку и выведет страницу
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == "GET":  # передаем конкретную задачу на вывод по id на редактирование
        form = TodoForm(instance=todo)  # создаем экз.класса (вывод формы на страницу)
        return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)  # передаем измененные данные в базу после редактирования формы
            form.save()  # сохраняем данные которые только-что  изменили в форме
            return redirect('currenttodos')  # перенаправляем пользователя на страницу с измененными данными
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form, 'error': 'Неверные данные'})


# Задача выполнена
def complete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('currenttodos')


# Вывод выполненных задач (Завершено)
def completed_todos(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'todo/completed_todos.html', {'todos': todos})


# Удаляем выполненные задачи
def delete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect('currenttodos')