from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from post.models import Post, Like
from .forms import ProfileForm, EditUserForm
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
def profile(request):
    profile = Profile.objects.filter(user = request.user).first()
    posts = Post.objects.filter(user = request.user).order_by('-created_at')
    liked_posts = Like.objects.filter(user=request.user).values_list('post_id', flat=True)
    form = PostForm()

    return render(request, 'core/profile.html', {
        'profile' : profile,
        'posts' : posts,
        'liked_posts' : liked_posts,
        'form' : form
    })

@login_required
def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('core:profile')
        
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'core/editProfile.html', {
        'user_form' : user_form,
        'profile_form' : profile_form,
        'profile' : profile
    })


@login_required
def logout_user(request):
    logout(request)
    return redirect('core:login')