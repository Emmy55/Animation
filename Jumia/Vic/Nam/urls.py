from . import views

from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('', views.page1, name="page1"),
    path('', views.page2, name="page2")
]