from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import SupNumProject, PersonalProject

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def project_list(request):
    supnum_projects = SupNumProject.objects.all()
    personal_projects = PersonalProject.objects.all()
    return render(request, 'project_list.html', {
        'supnum_projects': supnum_projects,
        'personal_projects': personal_projects
    })

@login_required
def new_project(request):
    if not request.user.is_superuser:
        return render(request, '403.html')
    return render(request, 'new_project.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})