from django.shortcuts import render

from .models import names

from django.http import HttpResponse
# Create your views here.

myname = names()
myname.id = 1
myname.name = "Emmanuel"
myname.des = "He is a developer"

sname = names()
sname.id = 2
sname.name = "Ayo"
sname.des = "He is a mobile app dev"

dname = names()
dname.id = 3
dname.name = "Bimpe"
dname.des = "She is a product designer"

def index(request):
    # return HttpResponse("Hello, World!")
    return render(request, "Ema/home.html", {
        'mynames' : myname,
        'snames' : sname,
        'dnames' : dname

    })

def about(request):
    return render(request, "Ema/about.html")
def contact(request):
    return render(request, "Ema/contact.html")
def team(request):
    return render(request, "Ema/team.html")

# def hello(request):
#     return HttpResponse("Hello, Emmanuel")

    
# def hello2(request):
#     return HttpResponse("Hello, Bolaji")

# def welcome(request):
#     return HttpResponse("Welcome to my page")

# def name(request, name):
#     return HttpResponse(f"<h1>Hello, {name}</h1>")


