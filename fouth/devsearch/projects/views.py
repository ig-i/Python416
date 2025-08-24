from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


def projects(request):
    pr = Project.objects.all()  # из модели Project берем все абсолютно данные
    contex = {
        'projects': pr
    }
    return render(request, "projects/projects.html", contex)  # скопировали готовый html документ


def project(request, pk):
    project_obj = Project.objects.get(id=pk)  # получаем запись из адресной строки по номеру id в html документ
    return render(request, "projects/single-project.html", {'project': project_obj})


@login_required(login_url="login")  # закрываем доступ другим пользователям
def create_project(request):  # пользователь заполняет форму и отправляет в проекты
    form = ProjectForm()  # экземпляр класса из forms.py (форма)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  # собираем данные из формы и передаем в базу (текст и файлы)
        if form.is_valid():  # если данные валидные (не подпадают под ограничения полей формы)  то он их сохраняет
            form.save()
        return redirect('projects')

    return render(request, 'projects/form-template.html', {'form': form})


