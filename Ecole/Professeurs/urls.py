from django.urls import path

from .views import *

app_name = 'Prof'
urlpatterns = [
    path('',Prof, name="Prof"),
]
