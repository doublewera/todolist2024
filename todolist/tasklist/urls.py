from django.urls import path, re_path
from . import views

urlpatterns = [
    # tasklist/  Приехало из глобального юрлз
    path('',                  views.index,         name='tasklist'),
    
    # tasklist/newtask/
    path('newtask/',          views.new_task,      name='new_task'),
    
    # tasklist/update_tasks/
    path('update_tasks/',     views.get_all_tasks, name='update'),

    # Calendar view
    path('calendar/',         views.calendar,      name='calendar_now'),

    # Calendar view
    path('calendar/<str:dtstr>/', views.calendar,      name='calendar'),
]
