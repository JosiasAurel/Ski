from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("skis/", views.skis, name="skis"),
    path("about/", views.about, name="about")
]
