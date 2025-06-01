# from django import forms
# from .models import Task

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'assignee', 'due_date', 'completed']  # Include all fields you need

# 25-05-2025

# asana/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'assignee', 'due_date', 'completed', 'priority', 'description']

