from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'), 
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/spunum/', views.project_list, name='supnum_projects'),
    path('projects/personnel/', views.project_list, name='personal_projects'),
    path('add_personal_project/', views.add_personal_project, name='add_personal_project'),
    path('groups/', views.group_list, name='group_list'),
]