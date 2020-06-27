from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login as login_module, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


@login_required(login_url='/login')
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        form = TaskForm(request.POST)
        newTask = form.save(commit=False)
        newTask.employee = request.user
        newTask.end_date = newTask.due_date
        newTask.save()
        return redirect('index')

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'GET':
            return render(request, 'login/index.html')
        else:
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'login/index.html', {'error': 'Username and password did not match'})
            else:
                login_module(request, user)
                return redirect('index')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'GET':
            return render(request, 'register/index.html')
        else:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.save()
                login_module(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'register/index.html', {'error': 'That username has already been taken. Please choose a new username'})
