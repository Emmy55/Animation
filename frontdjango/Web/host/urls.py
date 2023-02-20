from . import views

from django.urls import path

urlpatterns = [
    path('', views.first, name="first"),
    path('home', views.home, name="home"),
    path('signin', views.home1, name="home1"),
]