from django.db import models

class Ibovespa(models.Model):
    date = models.DateTimeField()
    open = models.FloatField(null=True, blank=True)
    high = models.FloatField(null=True, blank=True)
    low = models.FloatField(null=True, blank=True)
    close = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    dividends = models.FloatField(null=True, blank=True)
    stock = models.FloatField(null=True, blank=True)
    splits = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.date

class Dollar(models.Model):
    date = models.DateTimeField()
    open = models.FloatField(null=True, blank=True)
    high = models.FloatField(null=True, blank=True)
    low = models.FloatField(null=True, blank=True)
    close = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    dividends = models.FloatField(null=True, blank=True)
    stock = models.FloatField(null=True, blank=True)
    splits = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.date