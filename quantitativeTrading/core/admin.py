from re import search
from django.contrib import admin
from rangefilter.filters import DateRangeFilter

# Register your models here.

from .models import Ibovespa, Dollar, Bitcoin, Smal, SP_500, Xfix, Nasdaq


class base:
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


@admin.register(Ibovespa)
class IbovespaAdmin(base, admin.ModelAdmin):
    pass


@admin.register(Dollar)
class DollarAdmin(base, admin.ModelAdmin):
    pass


@admin.register(Bitcoin)
class BitcoinAdmin(base, admin.ModelAdmin):
    pass


@admin.register(Smal)
class SmalAdmin(base, admin.ModelAdmin):
    pass


@admin.register(SP_500)
class SP_500Admin(base, admin.ModelAdmin):
    pass


@admin.register(Xfix)
class XfixAdmin(base, admin.ModelAdmin):
    pass


@admin.register(Nasdaq)
class NadaqAdmin(base, admin.ModelAdmin):
    pass
