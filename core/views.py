from django.shortcuts import render
from .models import Dollar, Ibovespa, Bitcoin, Smal, Xfix, SP_500, Nasdaq


def index(request):
    info = {
        "title": "Quantitative Trading",
        "wdo": Dollar.objects.latest("Date"),
        "ind": Ibovespa.objects.latest("Date"),
        "btc": Bitcoin.objects.latest("Date"),
        "smal": Smal.objects.latest("Date"),
        "sp": SP_500.objects.latest("Date"),
        "xfix": Xfix.objects.latest("Date"),
        "nasdaq": Nasdaq.objects.latest("Date"),
    }
    return render(request, "core/home/index.html", {"info": info})
