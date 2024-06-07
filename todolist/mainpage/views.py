from django.shortcuts import render

def index(request):
    context = {}  
    return render(
        request,                # Запрос
	    'mainpage/index.html',  # путь к шаблону
        context                 # подстановки
    )