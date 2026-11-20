# All backend Logic will be written here. This is the place where we will write all the backend logic for our application.

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello, World! This is the home page of our Django application.</h1>")