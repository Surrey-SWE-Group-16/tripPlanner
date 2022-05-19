from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-index')

    else:
        # when sign up form fields are empty
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)


def profile(request):
    return render(request, 'users/profile.html')
