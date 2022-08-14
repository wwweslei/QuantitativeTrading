from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from .models import (
    SP_500,
    Bitcoin,
    Dollar,
    Ibovespa,
    Nasdaq,
    Portfolio,
    Smal,
    Stocks_overview,
    TheoreticalIbov,
    TheoreticalSmall,
    Xfix,
)


@admin.register(Bitcoin)
@admin.register(Xfix)
@admin.register(Smal)
@admin.register(SP_500)
@admin.register(Dollar)
@admin.register(Nasdaq)
@admin.register(Ibovespa)
class Register(admin.ModelAdmin):
    list_display = ("date", "open", "high", "low", "close", "volume")
    date_hierarchy = "date"
    search_fields = ["date"]
    list_filter = [("date", DateRangeFilter), ("date")]

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Portfolio)
class WalletAdmin(admin.ModelAdmin):
    pass


@admin.register(Stocks_overview)
class Stocks_overviewAdmin(admin.ModelAdmin):
    search_fields = ["symbol"]

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(TheoreticalIbov)
@admin.register(TheoreticalSmall)
class StocksIbovAdmin(admin.ModelAdmin):
    list_display = ("symbol", "name", "type", "quantity", "percentage")
    search_fields = ["symbol"]
    ordering = ["-percentage"]
    list_filter = ["type"]

    def has_change_permission(self, request, obj=None):
        return False
