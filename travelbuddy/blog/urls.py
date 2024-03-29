from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.index, name='blog-index'),    # if 1st parameter blank> main page, name= specifying name of url
    path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'), # function create in views
    path('post_delete/<int:pk>/', views.post_delete, name='blog-post-delete'),
    path('comment_delete/<int:pk>/', views.comment_delete, name='blog-comment-delete'),
]