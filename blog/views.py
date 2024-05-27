from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post
from .forms import BlogCreateForm, CommentForm

def home(request):
    posts = Post.objects.all().order_by('-id')
    featured_posts = Post.objects.filter(is_featured=True)[:2]
    
    context = {
        'posts': posts, 'featured_posts': featured_posts
    }
    return render(request, 'blog/home.html',context)

def show(request,id):
    post = Post.objects.get(id=id)
    context={'post': post}
    return render(request, 'blog/show.html', context)

@login_required
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

@login_required
def update(request, id):
    post = Post.objects.get(id=id)
    if not post.author == request.user:
        return redirect('/')
        
    if request.method == "POST":
        form = BlogCreateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BlogCreateForm(instance=post)
    context={'post': post, 'form': form}
    return render(request, 'blog/update.html', context)

@login_required
def create_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.comment_user=post.author
            comment_form.instance.post=post
            comment_form.save()
            return redirect('/')
    else:
        comment_form = CommentForm()    
    context={'comment_form': comment_form}
    return render(request, 'blog/add_comment.html', context)
