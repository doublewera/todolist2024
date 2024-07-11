from django.urls import path
from .views import index, new_task, get_all_tasks

urlpatterns = [
    # tasklist/  Приехало из глобального юрлз
    path('', index, name='tasklist'),
    
    # tasklist/newtask/
    path('newtask/', new_task, name='new_task'),
    
    # tasklist/update_tasks/
    path('update_tasks/', get_all_tasks, name='update')
]
