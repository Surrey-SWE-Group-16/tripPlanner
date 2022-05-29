from django.contrib import admin
from django.urls import path, include
from .views import user_map, get_maps, weather_api
from .import views


urlpatterns = [

    path('User/', views.user_map, name="user_map"),
    path('log/', views.user_log, name="planner-log"),
    path('log-delete/<int:pk>/', views.log_delete, name="delete-log"),
    path('log-history/<int:pk>/', views.user_log_history, name="planner-log-history"),

]