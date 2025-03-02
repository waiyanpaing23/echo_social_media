from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from core.models import Profile
from .models import Post, Like, Comment
from .forms import PostForm
from django.contrib.auth.models import User

@login_required
def index(request):
    profile = Profile.objects.filter(user=request.user).first()
    posts = Post.objects.annotate(like_count = Count('like'), comment_count = Count('comment')).order_by('-created_at')
    liked_posts = Like.objects.filter(user=request.user).values_list('post_id', flat=True)
    my_posts = Post.objects.filter(user=request.user)
    suggestions = User.objects.exclude(id=request.user.id).exclude(is_superuser=True)

    form = PostForm()

    return render(request, 'core/index.html',{
        'profile' : profile,
        'post_form' : form,
        'posts' : posts,
        'liked_posts' : liked_posts,
        'my_posts' : my_posts,
        'suggestions' : suggestions
    })

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            return redirect('core:index')
        else:
            form.add_error(None, 'Invalid post')

def like(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        like.delete()
        liked = False
    else:
        like = Like.objects.create(user=request.user, post=post)
        liked = True
    like_count = post.like_set.count()
    
    # return redirect('core:index')
    return JsonResponse({'liked': liked, 'like_count': like_count})

def comment(request, post_id):
    post = Post.objects.filter(id=post_id).first()

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')

        Comment.objects.create(user=request.user, post=post, comment_text=comment_text)

        return redirect('core:index')
        

        
