from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, "homepage.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def contactus(request):
    return render(request, "contactus.html")

def user(request):
    return render(request, "user.html")

def privacy(request):
    return render(request, "privacy.html")
