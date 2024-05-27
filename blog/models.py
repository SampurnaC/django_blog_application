from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    is_featured=models.BooleanField("IS FEATURED", default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_user=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField(max_length=200)

    def __str__(self):
        return f'{self.comment_user}Comment'
