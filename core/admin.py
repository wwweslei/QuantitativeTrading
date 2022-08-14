from django.contrib import admin

from .models import Portfolio, Stocks_overview


@admin.register(Portfolio)
class WalletAdmin(admin.ModelAdmin):
    pass


@admin.register(Stocks_overview)
class Stocks_overviewAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "last",
        "low",
        "high",
        "change",
        "change_percentage",
        "turnover",
    )
    search_fields = ["symbol"]
    ordering = ["-change_percentage"]

    def has_change_permission(self, request, obj=None):
        return False
