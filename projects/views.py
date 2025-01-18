from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import SupNumProject, PersonalProject
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Group

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




def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            # Vérifie si l'utilisateur existe déjà
            if User.objects.filter(username=username).exists():
                messages.error(request, "Le nom d'utilisateur est déjà pris.")
            else:
                # Crée un nouvel utilisateur
                User.objects.create_user(username=username, password=password)
                messages.success(request, "Votre compte a été créé avec succès.")
                return redirect('home')  # Redirection vers la page d'accueil après l'inscription
        else:
            messages.error(request, "Veuillez remplir tous les champs.")

    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')


def project_list(request):
    # Récupérer tous les projets SupNum et Personnel
    supnum_projects = SupNumProject.objects.all()
    personal_projects = PersonalProject.objects.all()

    # Rendre les projets SupNum dans la page supnum_projects.html
    if 'supnum' in request.path:
        return render(request, 'supnum_projects.html', {
            'supnum_projects': supnum_projects
        })

    # Rendre les projets personnels dans la page personal_projects.html
    elif 'personal' in request.path:
        return render(request, 'personal_projects.html', {
            'personal_projects': personal_projects
        })
    
    # Si aucune condition n'est remplie, renvoyer une page par défaut ou un message d'erreur
    return render(request, 'project_list.html', {
        'supnum_projects': supnum_projects,
        'personal_projects': personal_projects
    })

def add_personal_project(request):
    if not request.user.is_superuser:
        return redirect('personal_projects')  # Redirige si l'utilisateur n'est pas superuser

    if request.method == 'POST':
        name = request.POST.get('name')
        technologies = request.POST.get('technologies')
        semester = request.POST.get('semester')
        students_count = request.POST.get('students_count')

        PersonalProject.objects.create(
            name=name,
            technologies=technologies,
            semester=semester,
            students_count=students_count
        )
        return redirect('personal_projects')  # Redirige vers la liste des projets personnels

    return render(request, 'add_personal_project.html')




def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})