from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from finance.research.download_market_data import get_stocks_overview

from .forms import PortfolioForm
from .models import Stocks_overview


def index(request: HttpRequest) -> HttpResponse:
    """Render the index page.

    Args:
        request (HttpRequest): HTTP request
    Returns:
        HttpResponse: HTTP response
    """
    get_stocks_overview()
    overview_low = Stocks_overview.objects.all()
    overview_low = overview_low.order_by("change_percentage")[:25]
    overview_high = Stocks_overview.objects.all()
    overview_high = overview_high.order_by("-change_percentage")[:25]
    return render(
        request,
        "core/home/index.html",
        {
            "title": "Home",
            "overview_high": overview_high,
            "overview_low": overview_low,
        },
    )


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    """Render the profile page."""

    return render(
        request,
        "core/home/profile.html",
        {
            "title": "Profile",
        },
    )


def signup(request: HttpRequest) -> HttpResponse:
    """Render the register page."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso!")
            return redirect("home:index")
    form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def form_portfolio(request: HttpRequest) -> HttpResponse:
    """Render the form to create a portfolio."""
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    form = PortfolioForm()
    return render(
        request,
        "core/includes/form_portfolio.html",
        {"title": "Portfolio", "form": form},
    )
