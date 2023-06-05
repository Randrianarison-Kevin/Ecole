from django.urls import path
from .views import *

app_name = "Calendrier"
urlpatterns = [
    path("", Calendrier, name="Calendrier"),
]