from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('<slug:slug>', views.foldblog, name="foldblog"),

]