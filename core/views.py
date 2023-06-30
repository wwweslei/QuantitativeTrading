from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from finance.models import Stocks_overview


def index(request: HttpRequest) -> HttpResponse:
    """Render the index page."""
    # get_stocks_overview()
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
    msg = None
    success = False
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Usuário criado com sucesso."
            success = True
        else:
            msg = "Formulario invalido\ntente novamente."
    else:
        form = UserCreationForm()
    return render(
        request,
        "registration/signup.html",
        {"form": form, "msg": msg, "success": success},
    )
