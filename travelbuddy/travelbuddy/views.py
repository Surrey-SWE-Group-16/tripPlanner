from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return HttpResponse("Hello World!")


def index(request):
    return render(request, "testlogin.html")
