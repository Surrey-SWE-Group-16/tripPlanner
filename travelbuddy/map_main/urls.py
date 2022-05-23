from django.contrib import admin
from django.urls import path, include
from .views import user_map, get_maps, weather_api
from .import views


urlpatterns = [

    path('User/', views.user_map, name="user_map"),

]