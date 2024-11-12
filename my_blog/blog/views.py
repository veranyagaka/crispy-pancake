from django.shortcuts import render
from .models import Post
# Create your views here.
def all_blog_posts(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})