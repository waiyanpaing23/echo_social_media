from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from post.models import Post
from post.forms import PostForm

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('core:index')
            
            else:
                form.add_error(None, 'Invalid username or password')

    else:
        form = LoginForm()

        return render(request, 'core/login.html', {
            'form' : form
        })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            Profile.objects.create(user=user)

            return redirect('core:index')
        
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form' : form
    })

@login_required
def logout_user(request):
    logout(request)
    return redirect('core:login')