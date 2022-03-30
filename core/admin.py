from dataclasses import fields
from re import search
from django.contrib import admin
from rangefilter.filters import DateRangeFilter

# Register your models here.

from .models import Ibovespa, Dollar, Bitcoin, Smal, SP_500, Xfix, Nasdaq

@admin.register(Bitcoin)
@admin.register(Xfix)
@admin.register(Smal)
@admin.register(SP_500)
@admin.register(Dollar)
@admin.register(Nasdaq)
@admin.register(Ibovespa)
class Register(admin.ModelAdmin):
    fields = (
        "Date",
        "open",
        "close",
        "high",
        "low",
        "volume",
        "dividends",
        "stock_splits",
    )
    readonly_fields = fields
    list_display = ("Date", "open", "high", "low", "close", "volume")
    date_hierarchy = "Date"
    search_fields = ["Date"]
    list_filter = [("Date", DateRangeFilter), ("Date")]