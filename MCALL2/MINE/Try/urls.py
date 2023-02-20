from . import views

from django.urls import path

urlpatterns = [
    path('', views.lay, name="lay"),
    path('pick/', views.sel, name="sel"),
    path('add/', views.ads, name="ads"),
    path('sub/', views.sub, name="sub"),
    path('mult/', views.mult, name="mult"),
    path('div/', views.div, name="div"),
    path('squa/', views.squa, name="squa"),
    path('sqrt/', views.sqrt, name="sqrt"),
    path('simul/', views.simul, name="simul"),
    path('quad/', views.quad, name="quad"),
    # path('varia/', views.varia, name="varia"),
    path('selvaria/', views.selvaria, name="selvaria"),
    path('direct/', views.direct, name="direct"),
    path('inverse/', views.inverse, name="inverse"),
    # path('varia/', views.selvaria, name="selvaria"),
    # path('varia/', views.selvaria, name="selvaria"),
    path('ans/', views.ansbook, name="ansbook"),
    path('ans1/', views.ansbook1, name="ansbook1"),
    path('ans2/', views.ansbook2, name="ansbook2"),
    path('ans3/', views.ansbook3, name="ansbook3"),
    path('ans4/', views.ansbook4, name="ansbook4"),
    path('ans5/', views.ansbook5, name="ansbook5"),
    path('ans6/', views.ansbook6, name="ansbook6"),
    path('ans7/', views.ansbook7, name="ansbook7"),
    path('ans8/', views.ansbook8, name="ansbook8"),
    path('ans9/', views.ansbook9, name="ansbook9"),
    # path('ans9/', views.ansbook9, name="ansbook9"),

]