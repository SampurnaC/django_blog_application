from celery import shared_task
from .models import Post

@shared_task(bind=True)

def post_count(self):
    total_posts = Post.objects.count()
    return total_posts
