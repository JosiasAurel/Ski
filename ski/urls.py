from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("skis/", views.skis, name="skis"),
    path("about/", views.about, name="about"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register")
]
