from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.index, name='blog-index'),    # if 1st parameter blank> main page

]