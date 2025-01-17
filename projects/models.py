from django.db import models

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