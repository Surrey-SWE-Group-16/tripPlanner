from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return render(request, "testregister.html")


def index(request):
    return render(request, "testlogin.html")


def home(request):
    return render(request, "homepage.html")
