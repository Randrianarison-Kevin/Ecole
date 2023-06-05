
from django.urls import path
from .views import *

app_name = "Inscription"
urlpatterns = [
    path("", Inscription, name="Inscription"),    
]