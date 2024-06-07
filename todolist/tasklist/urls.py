from django.urls import path
from .views import index, new_task

urlpatterns = [
    path('', index, name='tasklist'),
    path('newtask/', new_task, name='new_task'),
]
