from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from core.finance import download_market_data

from .models import (SP_500, Bitcoin, Dollar, Ibovespa, Nasdaq, Smal,
                     Stocks_overview, Xfix)


def calc(obj) -> dict:
    """Calculate the percentage and variation of assets.

    Args:
        obj (models.Model): class object

    Returns:
        dict: dictionary with the percentage and last_value
    """
    query = obj.objects.all()[0:2]
    return {
        "pct": float(query[0].close / query[1].close - 1) * 100,
        "last_value": query[0].close,
    }


def index(request: HttpRequest) -> HttpResponse:
    """Render the index page.

    Args:
        request (HttpRequest): HTTP request
    Returns:
        HttpResponse: HTTP response"""

    download_market_data.run_all()
    card_info = {
        "wdo": calc(Dollar),
        "ind": calc(Ibovespa),
        "btc": calc(Bitcoin),
        "smal": calc(Smal),
        "sp": calc(SP_500),
        "xfix": calc(Xfix),
        "nasdaq": calc(Nasdaq),
    }
    overview_low = Stocks_overview.objects.all()
    overview_low = overview_low.order_by("change_percentage")[:20]
    overview_high = Stocks_overview.objects.all()
    overview_high = overview_high.order_by("-change_percentage")[:20]
    return render(
        request,
        "core/home/index.html",
        {
            "card_info": card_info,
            "title": "Quantitative Trading",
            "overview_high": overview_high,
            "overview_low": overview_low,
        },
    )
