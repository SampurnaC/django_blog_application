from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/<int:id>/', views.show, name='blog-show'),
    path('blog/create/', views.create, name='blog-create'),
    path('blog/<int:id>/update/', views.update, name='blog-update'),
    path('blog/<int:post_id>/comment/add', views.create_comment, name='create-comment'),
    
    
]
