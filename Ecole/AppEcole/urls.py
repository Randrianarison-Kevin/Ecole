from django.urls import path,include
from django import views

urlpatterns = [
    path('',views.home, name="home"),
]
