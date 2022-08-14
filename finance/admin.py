from django.contrib import admin

from .models import TheoreticalIbov, TheoreticalSmall


@admin.register(TheoreticalIbov)
@admin.register(TheoreticalSmall)
class StocksIbovAdmin(admin.ModelAdmin):
    list_display = ("symbol", "name", "type", "quantity", "percentage")
    search_fields = ["symbol"]
    ordering = ["-percentage"]
    list_filter = ["type"]

    def has_change_permission(self, request, obj=None):
        return False
