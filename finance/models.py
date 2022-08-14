from django.db import models


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
