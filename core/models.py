from django.db import models


class Stocks_overview(models.Model):
    country = models.TextField()
    name = models.TextField()
    symbol = models.TextField(primary_key=True)
    last = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    change = models.FloatField()
    change_percentage = models.FloatField()
    turnover = models.FloatField()
    currency = models.TextField()

    class Meta:
        db_table = "stocks_overview"
        verbose_name_plural = "stocks overview"

    def __str__(self):
        return f"{self.symbol}"
