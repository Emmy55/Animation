from django.urls import path

from . import views


urlpatterns = [
    path('mmodel', views.index, name="index"),
]