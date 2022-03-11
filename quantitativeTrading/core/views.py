import yfinance as yf
from django.shortcuts import render


def index(request):
    # ticket = "^BVSP"
    # ibovespa = yf.Ticker(ticket)
    # hist = ibovespa.history(period="max")
    # return render(request, "core/index.html",{'cota': hist.to_dict()})
    return render(request, "core/index.html")
