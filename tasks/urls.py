
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.home,name="home"),
    path('update_task/<int:pk>',views.update_task,name="udpate"),
    path("delete/<int:pk>",views.delete,name="delete")
]
