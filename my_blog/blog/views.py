from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
def all_blog_posts(request):
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user
        post = Post(title=title, content=content, author=author)
        post.save()
        return redirect('all_blog_posts')
    return render(request, 'add_post.html')

@login_required
def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user

        post.title = title
        post.content = content
        post.author = author

        post.save()
        return redirect('all_blog_posts')
    return render(request, 'edit_post.html', {'post':post})

@login_required
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('all_blog_posts')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_blog_posts')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})