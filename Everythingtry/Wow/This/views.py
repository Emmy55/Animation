from django.shortcuts import render

# Create your views here.

from .models import now

def index(request):
    seem = now.objects.all
    return render(request, 'This/index.html', {
        'print' : seem
    })