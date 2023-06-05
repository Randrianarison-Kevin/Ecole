from django.urls import path

from .views import *

app_name = 'Classes'
urlpatterns = [
    path('',Classes, name="Classes"),
]
