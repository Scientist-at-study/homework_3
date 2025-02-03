from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="course/photos/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=250, unique=True, null=True, blank=True)
    photo = models.ImageField(upload_to="student/photos/", null=True, blank=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
