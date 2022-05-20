from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests


# Create your views here.


def home(request):
    return render(request, "homepage.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "users/login.html")

def contactus(request):
    return render(request, "contactus.html")

def user(request):
    return render(request, "user.html")

def privacy(request):
    return render(request, "privacy.html")

def get_maps(request):
    loc = request.GET.get('location')
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+loc+"&key=AIzaSyD-AwK--sipbS9CBgDr9ipgUqvuYyk0tas"
    if request.method == 'GET':
        r = requests.post(url, params=request.GET)
        print(r.json())
    else:
        r = requests.get(url, params=request.GET)
        print(r.json())
    if r.status_code == 200:
        print(r.json())
        return JsonResponse(r.json())
    return JsonResponse(r.json())
def weather_api(request):
    lo = request.GET.get('longitude')
    la = request.GET.get('latitude')
    url = 'https://api.openweathermap.org/data/2.5/weather?lat='+la+'&lon='+lo+'&appid=64cb38ff5666d339a75fdba621c3ab81'
    if request.method == 'GET':
        r = requests.post(url, params=request.GET)
        print(r.json())
    else:
        r = requests.get(url, params=request.GET)
        print(r.json())
    if r.status_code == 200:
        print(r.json())
        return JsonResponse(r.json())
    return JsonResponse(r.json())
