from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts': posts})

def detail(request,post_id):
    blog_detail = get_object_or_404(Post , pk=post_id)
    return render(request,'detail.html', {'post':blog_detail})