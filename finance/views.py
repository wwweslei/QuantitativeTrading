from django.shortcuts import render

from finance.research import di, direct_treasure, etf, fii, index_b3, sgs, stock


def update(request):
    """Render the update page."""
    return render(
        request,
        "update.html",
        {
            "title": "Update",
        },
    )


def fii_update(request):
    """Render the update page."""
    fii.save()
    return render(
        request,
        "update.html",
        {
            "title": "Update",
        },
    )


def treasury_update(request):
    """Render the update page."""
    direct_treasure.save()
    return render(
        request,
        "update.html",
        {
            "title": "Update",
        },
    )


def di_update(request):
    """Render the update page."""
    di.save()
    return render(
        request,
        "update.html",
        {
            "title": "Update",
        },
    )


def etf_update(request):
    """Render the update page."""
    etf.save()
    return render(
        request,
        "update.html",
        {
            "title": "Update",
        },
    )


def stock_update(request):
    """Render the update page."""
    stock.save()
    return render(
        request,
        "update.html",
        {
            "title": "Update",
        },
    )


def index_b3_update(request):
    """Render the update page."""
    index_b3.save()
    return render(
        request,
        "update.html",
        {
            "title": "Update",
        },
    )


def sgs_update(request):
    """Render the update page."""
    sgs.save()
    return render(
        request,
        "update.html",
        {
            "title": "Update",
        },
    )
