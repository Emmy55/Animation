from . import views

from django.urls import path


urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('team', views.team, name="team"),

    
    # path('', views.index, name="index"),
    # path('', views.index, name="index"),
    # path('', views.index, name="index"),
    # path('emma', views.hello, name="hello"),
    # path('bolaji', views.hello2, name="hello2"),
    # path('welcome', views.welcome, name="hello2"),
    # path('<str:name>', views.name, name="myname")



]