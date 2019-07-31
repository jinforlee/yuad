from django.urls import path
from . import views

urlpatterns = [
    path('new_2', views.new_2),
    path('wrong_1', views.worng_1),
    path('wrong_2', views.wrong_2),
     path('new_3', views.new_3),
     path('final', views.final),
    path('list_', views.list_),
    path('wrong_', views.wrong_),

    
    ]
