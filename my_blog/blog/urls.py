from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_blog_posts, name='all_blog_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
]
