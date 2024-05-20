from django.shortcuts import render

posts = [
    {
        'name': 'Sam',
        'title': 'Software Engineer'
    },
    {
        'name': 'Sampurna',
        'title': 'Web Developer'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')
