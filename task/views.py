from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
# Create your views here.
def index(request):
  tasks = Task.objects.all()
  context = {
    'tasks' :tasks
  }
  return render(request, 'task/index.html', context)



def add_task(request):
  forms = TaskForm()

  if request.method == "POST":
    forms = TaskForm(request.POST)
    if forms.is_valid():
      forms.save()
      messages.success(request, 'Added New Task Sucessfully!')
      return redirect('index')
    
  context = {'forms': forms}
  forms = TaskForm()
  return render(request, 'task/addtask.html', context)



def update_task(request, pk):
  task = Task.objects.get(id=pk)
  forms = TaskForm(instance=task)

  if request.method == 'POST':
    forms = TaskForm(request.POST, instance=task)

    if forms.is_valid():
      forms.save()
      messages.success(request, f"'{task}' Updated Sucessfully!")
      return redirect('index')

  context = {'forms':forms}

  return render(request, 'task/updatetask.html', context)

def delete_task(request, pk):

  task = Task.objects.get(id=pk)
  task.delete()
  messages.success(request, f"'{task}' Deleted Sucessfully!")
  return redirect('index')
