from django.urls import path
from .views import index, new_task, get_all_tasks

urlpatterns = [
    path('', index, name='tasklist'),
    path('newtask/', new_task, name='new_task'),
    path('update_tasks/', get_all_tasks, name='update')
]
