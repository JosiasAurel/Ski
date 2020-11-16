from django.shortcuts import render
from django.http import HttpResponse
from .models import Snippet
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
