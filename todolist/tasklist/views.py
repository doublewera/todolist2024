from django.shortcuts import render

# Create your views here.

def index(request):
    tasks = [
        'Рассказать урок',
        'Дать задание',
        'Проверить задани',
        'Объяснить домашку',
    ]
    context = {
        'kogda': 'сегодня',
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
