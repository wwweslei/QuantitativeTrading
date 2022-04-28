from django.shortcuts import render
from django.db import models
from core.finance import download_market_data
from .models import Dollar, Ibovespa, Bitcoin, Smal, Xfix, SP_500, Nasdaq


def calc(obj: models.Model) -> dict:
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


def index(request):
    """Render the index page.

    Args:
        request (_type_): request object

    Returns:
        _type_: render template index.html
    """
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

    return render(
        request,
        "core/home/index.html",
        {"card_info": card_info, "title": "Quantitative Trading"},
    )
