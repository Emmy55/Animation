from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import *

def indexView(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
    }
    return render(request, 'index.html', context)


def getCourses(request):
    category = request.Get.get('category')
    category = Category.objects.filter(category=category)
    courses = list(Course.objects.filter(category__in=category).values('Courses_Name'))
    response_data = {
        "courses": courses
    }
    return JsonRespone(response_data)