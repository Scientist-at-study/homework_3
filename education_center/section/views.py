from django.shortcuts import render

from django.http import (HttpRequest, HttpResponse)

# Create your views here.

from .models import Course, Student

def index(request: HttpRequest):
    course = Course.objects.all()
    student = Student.objects.all()
    context = {
        "course": course,
        "student": student,
    }
    return render(request, "index.html", context)