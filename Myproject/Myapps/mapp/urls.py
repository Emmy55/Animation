from . import views

from django.urls import path
urlpatterns = [

    path('try/', views.name, name="name1"),
    path('try2/', views.name2, name="name2"),
    path('ans/', views.ans, name="answer")
]