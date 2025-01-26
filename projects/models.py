from django.db import models
from django.contrib import admin

class SupNumProject(models.Model):
    name = models.CharField(max_length=255)
    technologies = models.TextField()
    supervisor = models.CharField(max_length=255)
    semester = models.CharField(max_length=50)
    max_students = models.IntegerField()

    def __str__(self):
        return self.name

class PersonalProject(models.Model):
    name = models.CharField(max_length=255)
    technologies = models.TextField()
    semester = models.CharField(max_length=50)
    students_count = models.IntegerField()

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=255)  # Nom du groupe
    project_name = models.CharField(max_length=255)  # Nom du projet
    project_type = models.CharField(
        max_length=20,
        choices=[('SupNum', 'SupNum'), ('Personnel', 'Personnel')],
        default='SupNum',
    )  # Type de projet
    student_names = models.TextField(
        help_text="Entrez les noms des étudiants séparés par des virgules"
    )  # Noms des étudiants (séparés par des virgules)

    def __str__(self):
        return self.name

    def student_list(self):
        """Retourne une liste des noms des étudiants"""
        return [name.strip() for name in self.student_names.split(",") if name.strip()]

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_name', 'project_type')
