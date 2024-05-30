from django.contrib import admin
from .models import Task
 
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.get_fields()]

