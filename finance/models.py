from django.db import models


class Theoretical(models.Model):
    symbol = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    quantity = models.TextField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class TheoreticalIbov(Theoretical, models.Model):
    class Meta:
        db_table = "theoretical_ibov"
        verbose_name_plural = "theoretical Ibovespa"


class TheoreticalSmall(Theoretical, models.Model):
    class Meta:
        db_table = "theoretical_Small"
        verbose_name_plural = "theoretical small"


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


class Stocks_br(models.Model):
    symbol = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    isin = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "stocks_br"
        verbose_name_plural = "Stocks Brazil"

    def __str__(self):
        return f"{self.name}"


class Fii(models.Model):
    symbol = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "fiis"
        verbose_name_plural = "FII Brazil"

    def __str__(self):
        return f"{self.name}"


class SectorClassification(models.Model):
    symbol = models.TextField(primary_key=True)
    listing = models.TextField(max_length=10)
    economic_sector = models.TextField(max_length=100)
    sub_sector = models.TextField(max_length=100)
    segment = models.TextField(max_length=100)

    class Meta:
        db_table = "sector_classification"
        verbose_name_plural = "Sector Classification"

    def __str__(self):
        return f"{self.symbol} {self.economic_sector}"
