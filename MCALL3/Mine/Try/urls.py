from . import views 
from django.urls import path



urlpatterns =  [
    path('', views.home, name="home"),
    path('sub/', views.sub, name="sub"),
    path('ans/', views.ans, name="ans"),
    path('ans1/', views.ans1, name="ans1"),
    # path('sub/', views.sub, name="sub"),
    path('mult/', views.mult, name="mult"),
    # path('div/', views.div, name="div"),
    # path('squa/', views.squa, name="squa"),
    # path('sqrt/', views.sqrt, name="sqrt"),
]