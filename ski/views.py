from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, request
from .models import Snippet
from .forms import SkiUserCreationForm
from django.contrib.auth import login
# Create your views here.


def home(request):
    return render(request, "index.html", {})


def skis(request):
    ski_objs = Snippet.objects.all()
    _ski_ctx = {
        'skis': ski_objs
    }
    return render(request, "skis.html", _ski_ctx)


def about(request):
    return render(request, "about.html", {})


def register(request):
    if request.method == "GET":
        form_ctx = {
            "form": SkiUserCreationForm
        }
        return render(request, "registration/register.html", form_ctx)

    elif request.method == "POST":
        form = SkiUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("skis"))
