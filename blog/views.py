from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def show(request,id):
    post = Post.objects.get(id=id)
    context={'post': post}
    return render(request, 'blog/show.html', context)
