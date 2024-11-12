from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_blog_posts, name='all_blog_posts')
]
