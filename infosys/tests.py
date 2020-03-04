from django.test import TestCase
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

# Create your tests here.
def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'list.html', context)