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
        context               # подстановки
    )

