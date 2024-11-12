from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=199)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'blog_post'