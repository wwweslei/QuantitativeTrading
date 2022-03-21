from django.shortcuts import render
from .models import Dollar, Ibovespa, Bitcoin, Smal, Xfix, SP_500, Nasdaq


def index(request):
    info = {
        "title": "Quantitative Trading",
        "wdo": Dollar.objects.latest("date"),
        "ind": Ibovespa.objects.latest("date"),
        "btc": Bitcoin.objects.latest("date"),
        "smal": Smal.objects.latest("date"),
        "sp": SP_500.objects.latest("date"),
        "xfix": Xfix.objects.latest("date"),
        "nasdaq": Nasdaq.objects.latest("date"),
    }
    return render(request, "core/home/index.html", {"info": info})
