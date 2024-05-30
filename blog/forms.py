from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'content', 'is_featured']
        labels = {'content': 'Body', 'is_featured': 'Is Featured'}
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'add your title here', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'add your content here', 'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['body']
        labels = {'body': ''}
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'add your comments here'}),
        }
