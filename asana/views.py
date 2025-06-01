# from django.shortcuts import render

# # Create your views here.

# from django.shortcuts import render
# from .models import Task

# def task_list(request):
#     tasks = Task.objects.all().order_by('-created_at')
#     return render(request, 'asana/task_list.html', {'tasks': tasks})


# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib import messages
# from .models import Task
# from .forms import TaskForm  # Assuming you will create this form

# # View to display the task list
# def task_list(request):
#     tasks = Task.objects.all()  # Fetch all tasks from the database
#     return render(request, 'asana/task_list.html', {'tasks': tasks})

# # View to edit a task
# def task_edit(request, task_id):
#     task = get_object_or_404(Task, id=task_id)  # Fetch task by ID
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)  # Bind form with task data
#         if form.is_valid():
#             form.save()  # Save the updated task
#             messages.success(request, 'Task updated successfully!')
#             return redirect('task_list')  # Redirect back to the task list
#     else:
#         form = TaskForm(instance=task)  # Pre-fill the form with existing task data
#     return render(request, 'asana/task_edit.html', {'form': form, 'task': task})

# # View to delete a task
# def task_delete(request, task_id):
#     task = get_object_or_404(Task, id=task_id)  # Fetch task by ID
#     task.delete()  # Delete the task
#     messages.success(request, 'Task deleted successfully!')
#     return redirect('task_list')  # Redirect back to the task list

# def task_list(request):
#     query = request.GET.get('q')
#     status = request.GET.get('status')

#     tasks = Task.objects.all()

#     if query:
#         tasks = tasks.filter(title__icontains=query)

#     if status == 'completed':
#         tasks = tasks.filter(completed=True)
#     elif status == 'incomplete':
#         tasks = tasks.filter(completed=False)

#     return render(request, 'asana/task_list.html', {'tasks': tasks})

#     sort = request.GET.get('sort')
#     if sort == 'due':
#         tasks = tasks.order_by('due_date')
#     elif sort == 'title':
#         tasks = tasks.order_by('title')


# 25-05-2025

# asana/views.py
from django.shortcuts import render
from django.db.models import Q
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    
    # Search filter
    search_query = request.GET.get('q', '')
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    return render(request, 'asana/task_list.html', {'tasks': tasks, 'search_query': search_query})

# asana/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Edit Task View
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('asana:task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'asana/task_edit.html', {'form': form, 'task': task})

# Delete Task View
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect('asana:task_list')
    
    return render(request, 'asana/confirm_delete.html', {'task': task})
