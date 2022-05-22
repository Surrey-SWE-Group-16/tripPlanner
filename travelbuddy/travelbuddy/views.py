from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import MapModel, ChecklistModel, JournalModel
from .forms import MapModelForm, ChecklistModelForm, JournalModelForm
from django.contrib.auth.decorators import login_required

"""
Isak and Adrian's code
"""
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

"""
Isak and Adrian's code end
"""

# Map location can only be viewed when logged in
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

# Map detail can only be viewed when logged in
# @login_required
# # pk for primary key
# def checklist(request, pk):
#     post = PostModel.objects.get(id=pk)
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             instance = comment_form.save(commit=False)
#             instance.user = request.user
#             instance.post = post
#             instance.save()
#             return redirect('blog-post-detail', pk=post.id)
#     else:
#         comment_form = CommentForm()
#     context = {
#         'post': post,
#         'comment_form': comment_form,
#     }
#     return render(request, 'blog/post_detail.html', context)
#
# # post can only be edited when logged in
# @login_required
# def post_edit(request, pk):
#     # grab post
#     post = PostModel.objects.get(id=pk)
#     if request.method == 'POST':
#         form = PostUpdateForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('blog/post_detail', pk=post.id)
#     else:
#         form = PostUpdateForm(instance=post)
#     context = {
#         'post': post,
#         'form': form,
#     }
#     return render(request, 'blog/post_edit.html', context)
#
# # post can only be deleted when logged in
# @login_required
# def post_delete(request, pk):
#     post = PostModel.objects.get(id=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('blog-index')
#     context = {
#         'post': post
#     }
#     return render(request, 'blog/post_delete.html', context)
#
# # comment can only be deleted when logged in
# @login_required
# def comment_delete(request, pk):
#     comment = Comment.objects.get(id=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             # request.user=logged in user
#             instance.author = request.user
#         comment.delete()
#         return redirect('blog-post-detail', pk=comment.post.id)
#     context = {
#         'comment': comment
#     }
#     return render(request, 'blog/comment_delete.html', context)
#
