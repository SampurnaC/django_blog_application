from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import BlogCreateForm, CommentForm
from .documents import PostDocument
from elasticsearch_dsl.query import MultiMatch
 
def home(request):
    featured_posts = Post.objects.filter(is_featured=True)[:5]
    
    if 'q' in request.GET:
        q = request.GET['q']
        query = MultiMatch(query=q, fields=["title", "content"], fuzziness="AUTO")
        posts = PostDocument.search().query(query).to_queryset()
    else:
        posts = Post.objects.all().order_by('-id')
    context = {
        'posts': posts
    }
    
    context = {
        'posts': posts, 'featured_posts': featured_posts
    }
    return render(request, 'blog/home.html',context)

def featured(request):
    featured_posts = Post.objects.filter(is_featured=True)
    context={'featured_posts': featured_posts}
    return render(request, 'blog/featured.html', context)
    
def show(request,id):
    post = Post.objects.get(id=id)
    related_posts = Post.objects.all().exclude(id=id)[:3]
    
    comments = post.comments.all().order_by('-id')
    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.comment_user=request.user
            comment_form.instance.post=post
            comment_form.save()
            return redirect('/')
    else:
        comment_form = CommentForm()    
    context={'comment_form': comment_form, 'comments': comments, 'post': post, 'related_posts': related_posts}
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
def update_comment(request,post_id, comment_id):
    post=Post.objects.get(id=post_id)
    comment = Comment.objects.get(id=comment_id)
    if not comment.comment_user == request.user:
        return redirect('/')
        
    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('blog:blog-show', post.id)
    else:
        comment_form = CommentForm(instance=comment)    
    context={'comment_form': comment_form, 'comment': comment, 'post': post}
    return render(request, 'blog/update_comment.html', context)


def search(request,q):
    q = request.GET.get("q")
    context={}
    if q:
        s = PostDocument.search().query("match", title=q)
        context["posts"] = s
    return render(request, "blog/search.html")
