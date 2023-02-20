from . import views

from django.urls import path

urlpatterns = [
    path('', views.indexView, name='Home'),
    path('get-courses/', views.getCourses, name='GetCourses'),
]
