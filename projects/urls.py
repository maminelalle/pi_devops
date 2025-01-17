from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/new/', views.new_project, name='new_project'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]