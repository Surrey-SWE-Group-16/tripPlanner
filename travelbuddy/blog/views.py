from django.shortcuts import render, redirect
from .models import PostModel, Comment
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# blog can only be viewed when logged in
@login_required
# Creating post
def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # request.user=logged in user
            instance.author = request.user
            instance.save()
            # blog url in blog urls
            return redirect('blog-index')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form': form,
    }

    return render(request, 'blog/index.html', context)

# post detail can only be viewed when logged in
@login_required
# pk for primary key
def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)

# post can only be edited when logged in
@login_required
def post_edit(request, pk):
    # grab post
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog/post_detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)

# post can only be deleted when logged in
@login_required
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post': post
    }
    return render(request, 'blog/post_delete.html', context)

# comment can only be deleted when logged in
@login_required
def comment_delete(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # request.user=logged in user
            instance.author = request.user
        comment.delete()
        return redirect('blog-post-detail', pk=comment.post.id)
    context = {
        'comment': comment
    }
    return render(request, 'blog/comment_delete.html', context)
