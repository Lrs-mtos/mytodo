from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def list_tasks(request):
    tasks = Task.objects.all()  # Obtém todas as tarefas do banco de dados
    return render(request, 'tasks/list_tasks.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return HttpResponseRedirect(reverse('list_tasks'))

def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return HttpResponseRedirect(reverse('list_tasks'))

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_tasks')
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_tasks')  # Redireciona para a página inicial após o signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')