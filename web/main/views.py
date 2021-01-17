from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def home(request):
    return render(request, 'main/home.html')


def my_works(request):
    tasks = Task.objects.order_by('-id')
    dic = {'tasks':tasks}
    return render(request, 'main/my_works.html', dic)


def login(request):
    return render(request, 'registration/login.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верная'
    form = TaskForm()
    dic = {
        'form': form
    }
    return render(request, 'main/create.html', dic)