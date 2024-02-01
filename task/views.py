from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

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
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
    
  context = {'forms': forms}
    
  form = TaskForm
  return render(request, 'task/addtask.html', context)



def update_task(request, pk):
  task = Task.objects.get(id=pk)
  forms = TaskForm(instance=task)

  if request.method == 'POST':
    form = TaskForm(request.POST, instance=task)

    if form.is_valid():
      form.save()
      return redirect('index')

  context = {'forms':forms}

  return render(request, 'task/updatetask.html', context)

def delete_task(request, pk):

  task = Task.objects.get(id=pk)

  if request.method == 'POST':
    task.delete()
    return redirect('index')

  context = {'task': task}

  return render(request, 'task/deletetask.html', context)
