from django.shortcuts import render

# Create your views here.

from .models import Sold



def home(request):
    a_big_div = Sold.objects.all
    return render(request, 'mine/home.html', {
        'las' : a_big_div
    })

def login(request):
    return render(request, 'mine/login.html')

def foldblog(request, slug):
    sext = Sold.objects.get(slug=slug)
    return render(request, 'mine/foldblog.html', {
        'past' : sext
    })