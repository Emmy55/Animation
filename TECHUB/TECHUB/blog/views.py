from django.shortcuts import render

# Create your views here.
from .models import Blog

def home(request):
    blog = Blog.objects.all()
    return render(request, 'blog/home.html', {
        'blog' : blog
    })

def blogpost(request, slug):
    post = Blog.objects.get(slug=slug)
    return render(request, 'blog/blogpost.html', {
        'post' : post
    })
def about(request):
    return render(request, 'blog/about.html')
def contact(request):
    return render(request, 'blog/contact.html')
def team(request):
    return render(request, 'blog/team.html')
def login(request):
    return render(request, 'blog/login.html')
def signup(request):
    return render(request, 'blog/signup.html')