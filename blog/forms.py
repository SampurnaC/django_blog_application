from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'content', 'is_featured']


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3}),
        }
