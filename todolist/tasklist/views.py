from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from datetime import datetime

def get_all_tasks(request):
    print(request.method)
    print(request.body)
    #tasks = Task.objects.all()
    return JsonResponse(
        {'mydata': 'Молодец, уже лучше!'}
    )


def index(request):
    tasks = Task.objects.filter(
        deadline__gte='2024-06-11'
    )
    # Вытащить из БД все объекты типа Task
    context = {
        'kogda': 'сегодня',
        'tasks': tasks,
    }
    return render(
        request,                # Запрос
	    'tasklist/index.html',  # путь к шаблону
        context                 # подстановки
    )

from .forms import TaskForm

def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    #else:
    context = {
        'form': TaskForm(),
    }
    return render(
        request,                  # Запрос
	    'tasklist/newtask.html',  # путь к шаблону
        context                   # подстановки
    )
