from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import MapModel
from .forms import MapModelForm
from django.contrib.auth.decorators import login_required
import requests


def user_map(request):
    # print(MapModelForm.)
    # map_mod = MapModelForm.objects.all()
    # print("daefefeafaf

    if request.method == 'POST':
        form = MapModelForm(request.POST, request.FILES )

        print(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            # request.user=logged in user

            instance.author = request.user
            instance.save()
            # blog url in blog urls
            return redirect('blog-index')
    else:
        form = MapModelForm()



    #     form = MapModelForm()
    # context = {
    #     'posts': map_mod,
    #     'form': form,
    #
    # }
    return render(request, "map_main/user.html", {'form': form})


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
# Create your views here.


def weather_api(request):
    lo = request.GET.get('longitude')
    la = request.GET.get('latitude')
    url = 'https://api.openweathermap.org/data/2.5/weather?lat='+la+'&lon='+lo+'&units=metric&appid=64cb38ff5666d339a75fdba621c3ab81'
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


@login_required
# Creating post
def location(request):
    points = MapModel.objects.all()
    if request.method == 'POST':
        form = MapModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # request.user=logged in user
            instance.user = request.user
            instance.save()
            # blog url in blog urls
            return redirect('location')
    else:
        form = MapModelForm()
    context = {
        'points': points,
        'form': form,
    }

    return render(request, 'planner/location.html', context)

