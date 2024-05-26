from django.shortcuts import render, redirect
from .models import Post
from .forms import BlogCreateForm

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

def create(request):
    if request.method == "POST":
        form = BlogCreateForm(request.POST)
        if form.is_valid():
            form.instance.author=request.user
            form.save()
            return redirect('/')
    else:
        form = BlogCreateForm()    
    context = {'form': form}
    return render(request, 'blog/create.html', context)
