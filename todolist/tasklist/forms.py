from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        #fields = [field.name for field in Task._meta.get_fields()]
        fields = [
            'deadline',
            'description'
        ]
        labels = {
            "given": "Задача выдана",
        }
        widgets = {
            #'given' :   forms.DateInput(attrs={'type':'datetime-local'}),
            'deadline': forms.DateInput(attrs={'type':'datetime-local'}),
            #'category': forms.TextInput(attrs={'type':'color'}),
        }