from . import views
from django.urls import path


urlpatterns = [
    path('sing', views.nite, name="sam"),
    # path('sign', views.sam1, name="sam1"),
    
]