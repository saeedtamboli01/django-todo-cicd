from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    tasks = Todo.objects.all()
    return render(request, 'todos/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Todo.objects.create(title=title)
        return redirect('index')
    return render(request, 'todos/add_task.html')
