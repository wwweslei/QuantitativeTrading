
from django.shortcuts import render


def index(request):
    info= {"title": "Quantitative Trading"}
    return render(request, "core/home/index.html", {"info": info})
