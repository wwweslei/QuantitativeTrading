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
