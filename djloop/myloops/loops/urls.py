from . import views
from django.urls import path


urlpatterns = [
    path('loops', views.index, name="index"),
]