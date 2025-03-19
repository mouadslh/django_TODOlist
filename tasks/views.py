from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
            
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/task_list.html', context)

def complete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')