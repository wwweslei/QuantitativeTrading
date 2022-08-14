from django.db import models


class Portfolio(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    date = models.DateField()
    symbol = models.CharField(max_length=10)
    value = models.FloatField()
    total_value = models.FloatField()
    qtd = models.IntegerField()

    class Meta:
        db_table = "portfolio"
        verbose_name_plural = "portfolio"

    def __str__(self):
        return f"{self.user} {self.symbol}"


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
