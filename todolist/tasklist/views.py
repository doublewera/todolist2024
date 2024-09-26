from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task
from datetime import datetime, timedelta
import json

def task_desc(tasks):
    result = []
    for t in tasks:
        result.append(t.description)
    return result

def get_all_tasks(request):
    print('MY METHOD', request.method)
    print('MY BODY', request.body)
    json_str = request.body.decode('utf-8')
    json_objs = json_str.split('\n')
    json_request = json.loads(json_objs[0])
    tasks = Task.objects.filter(
        deadline__gte=json_request['dt']   #'2024-07-10' gte >= lte <=
    )
    return JsonResponse(
        {'mydata': 'Молодец, уже лучше!',
         'tasks': task_desc(tasks)}
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
    return render(              # HttpResponse
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

# timeslots = {
#    '10:00': {
#            'time': '10:00',
#            'weekdays': [
#                {'free': True},  # 0
#                {'free': True},  # 0
#                {'free': True},  # 0
#                {'free': True},  # 0
#                {'free': True},  # 0
#                {'free': True},  # 0
#                {'free': True},  # 0
#            ]
#        }
# }
def newWeek(dt):
    work_starts = 10   # 10:00 утра
    slots_per_day = 23  # 12 по полчаса
    # Создадим слоты
    timeslots = {}
    s = datetime(dt.year, dt.month, dt.day, work_starts)
    while s < dt + timedelta(7):  # next week
        wd = []
        for i in range(7):
            wd.append({
                'free': True
            })
        tm = s.strftime('%H:%M')
        timeslots[tm] = {
            'time': tm,
            'weekdays': wd
        }
        s += timedelta(seconds=1800)  # 3600 = 60*60 - это час в секундах
        if s.hour > work_starts + slots_per_day / 2:
            s += timedelta(1)
            s = datetime(s.year, s.month, s.day, work_starts)
    return timeslots

def calendar(request, dtstr=''):
    dt = datetime.now()
    try:
        dt = datetime.strptime(dtstr, '%Y%m%d')
    except:
        return redirect(dt.strftime('/tasklist/calendar/%Y%m%d'))
    if dt.weekday():  # 0 - понедельник
        return redirect((dt - timedelta(dt.weekday())).strftime('/tasklist/calendar/%Y%m%d'))
    dt_next = dt + timedelta(7)  # next week
    timeslots = newWeek(dt)

    # Все задачи на эту неделю
    tasks = Task.objects.filter(  # Достаточно фильтровать по одному параметру, если все слоты умещаются в текущие сутки и никто заполночь не работает
        deadline__gte=dt.strftime('%Y-%m-%d')
    ).filter(deadline__lte=dt_next.strftime('%Y-%m-%d'))
    print(tasks)
    for t in tasks:
        tm = t.softline.strftime('%H:%M')
        #print(t.description, t.softline, tm)
        #print(timeslots[tm])
        if tm in timeslots:
            s = timeslots[tm]['weekdays'][t.softline.weekday()]
            s['free'] = False
            s['task'] = t
    # Превращаем в список, чтобы потом не мучиться упорядочиваением
    timeslots_list = []
    for key in sorted(list(timeslots.keys())):
        timeslots_list.append(timeslots[key])
    context = {
        'prev_week': (dt - timedelta(7)).strftime('%Y%m%d'),
        'curr_week': (dt).strftime('%Y%m%d'),
        'next_week': (dt + timedelta(7)).strftime('%Y%m%d'),
        'timeslots': timeslots_list
    }
    return render(
        request,                    # Запрос
	    'tasklist/calendar.html',   # путь к шаблону
        context                     # подстановки
    )
