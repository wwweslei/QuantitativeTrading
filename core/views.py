from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from core.forms import PortifolioUserForm
from core.graph import treasure_graph
from core.graph_di import graph_di
from core.models import PortifolioUser
from finance.models import Stocks_overview


def index(request: HttpRequest) -> HttpResponse:
    """Render the index page."""
    # overview = Stocks_overview.objects.all()
    # overview_low = overview.order_by("change_percentage")[:25]
    # overview_high = overview.order_by("-change_percentage")[:25]
    return render(
        request,
        "core/home/index.html",
        {
            "title": "Home",
            # "overview_high": overview_high,
            # "overview_low": overview_low,
        },
    )


def treasure(request: HttpRequest) -> HttpResponse:
    """Render the index page."""
    treasure_graph()
    return render(
        request,
        "core/home/treasure.html",
        {
            "title": "Tesouro Direto",
        },
    )


def di(request: HttpRequest) -> HttpResponse:
    """Render the index page."""
    graph_di()
    return render(
        request,
        "core/home/di.html",
        {
            "title": "DI",
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


def portifolio_user_form(request: HttpRequest) -> HttpResponse:
    """Render the form page."""

    portifolio_user = PortifolioUser()
    form = PortifolioUserForm()
    if request.method == "POST":
        form = PortifolioUserForm(request.POST)
        if form.is_valid():
            portifolio_user.user_id = request.user.id
            portifolio_user.type = form.cleaned_data["type"]
            portifolio_user.cod = form.cleaned_data["cod"]
            portifolio_user.quantity = form.cleaned_data["quantity"]
            portifolio_user.price = form.cleaned_data["price"]
            portifolio_user.date = form.cleaned_data["date"]
            portifolio_user.save()
            return redirect("/accounts/profile/")
    return render(
        request,
        "core/profile/portifolio_user_form.html",
        {"form": form},
    )
