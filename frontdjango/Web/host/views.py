from django.shortcuts import render

from .models import Sam
# Create your views here.

mine = Sam()
id = 1
mine.name = "OPEN PRACTICAL UI/UX"
mine.des = " Design <br> Revolution Open And Practical Learning User Experience <br> and User Interface design for beginners."

sine = Sam()
id = 2
sine.name = "I'm Really Glad"
sine.des = "Wooooooooooooow this is nice"

dine = Sam()
id = 3
dine.name = "Order!"
dine.des = "I want to amaze you today"


from django.http import HttpResponse

def first(request):
    return render(request, "host/layout.html")

def home(request):
    return render(request, "host/home.html", {
        'mine1' : mine,
        "sine1" :sine,
        'dine1' : dine
    })
def home1(request):
    return render(request, "host/second.html")