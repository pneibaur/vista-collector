from unicodedata import name
from django.urls import path
from . import views
import vistas_collector

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("vistas/", views.vistas_index, name="index")
]
