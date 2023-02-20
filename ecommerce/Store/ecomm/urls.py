from . import views

from django.urls import path




urlpatterns = [
    path('', views.shop, name="shop"),
    path('shop/', views.shop1, name="shop1")
]