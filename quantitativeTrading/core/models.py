from tabnanny import verbose
from django.db import models


class base(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    dividends = models.IntegerField(blank=True, null=True)
    stock_splits = models.IntegerField(db_column="stock splits", blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.date.strftime("%d-%m-%Y")


class Ibovespa(base, models.Model):
    class Meta:
        db_table = "ibovespa"
        verbose_name_plural = "Ibovespa"


class Dollar(base, models.Model):
    class Meta:
        db_table = "dollar"
        verbose_name_plural = "Dollar"


class Bitcoin(base, models.Model):
    class Meta:
        db_table = "bitcoin"
        verbose_name_plural = "Bitcoin"


class Smal(base, models.Model):
    class Meta:
        db_table = "smal"
        verbose_name_plural = "Small"


class SP_500(base, models.Model):
    class Meta:
        db_table = "sp_500"
        verbose_name = "S&P 500"
        verbose_name_plural = "S&P 500"


class Xfix(base, models.Model):
    class Meta:
        db_table = "xfix"
        verbose_name_plural = "Xfix"


class Nasdaq(base, models.Model):
    class Meta:
        db_table = "nasdaq"
        verbose_name_plural = "Nasdaq"
