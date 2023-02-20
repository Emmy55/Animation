from . import views

from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('team', views.team, name="team"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('<slug:slug>', views.blogpost, name="blogpost"),
]