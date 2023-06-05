from django.urls import path

from .views import *

app_name = 'Apropos'
urlpatterns = [
    path('',Apropos, name="Apropos"),
]
