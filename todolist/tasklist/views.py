from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()
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
