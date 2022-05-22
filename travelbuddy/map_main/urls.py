from django.contrib import admin
from django.urls import path, include
from .views import user, get_maps, weather_api
from django.contrib.auth import views as auth_view


urlpatterns = [

    path('User/', auth_view.LogoutView.as_view(template_name='map_main/user.html'), name="user-map"),

]