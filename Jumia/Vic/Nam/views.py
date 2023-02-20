from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Nam/index.html")

def page1(request):
    return render(request, "page1.html")

def page2(request):
    return render(request, "page2.html")

    