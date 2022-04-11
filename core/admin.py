from dataclasses import fields
from re import search
from django.contrib import admin
from rangefilter.filters import DateRangeFilter

# Register your models here.

from .models import Ibovespa, Dollar, Bitcoin, Smal, SP_500, Xfix, Nasdaq, Portfolio, Stocks_overview
@admin.register(Bitcoin)
@admin.register(Xfix)
@admin.register(Smal)
@admin.register(SP_500)
@admin.register(Dollar)
@admin.register(Nasdaq)
@admin.register(Ibovespa)
class Register(admin.ModelAdmin):
    fields = (
        "date",
        "open",
        "close",
        "high",
        "low",
        "volume",
        "dividends",
        "stock_splits",
    )
    readonly_fields = fields
    list_display = ("date", "open", "high", "low", "close", "volume")
    date_hierarchy = "date"
    search_fields = ["date"]
    list_filter = [("date", DateRangeFilter), ("date")]
    
@admin.register(Portfolio)
class WalletAdmin(admin.ModelAdmin):
    pass

@admin.register(Stocks_overview)
class Stocks_overviewAdmin(admin.ModelAdmin):
    search_fields = ["symbol"]
    pass
