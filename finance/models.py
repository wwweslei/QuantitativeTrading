# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class Aall34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AALL34"


class Aalr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AALR3"


class Aapl34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AAPL34"


class Abbv34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ABBV34"


class Abcb10(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ABCB10"


class Abcb4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ABCB4"


class Abcp11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ABCP11"


class Abev3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ABEV3"


class Abtt34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ABTT34"


class Acnb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ACNB34"


class Adhm3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ADHM3"


class Aflt3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AFLT3"


class Agro3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AGRO3"


class Agronegocio(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "AGRONEGOCIO"


class Aheb3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AHEB3"


class Aigb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AIGB34"


class Almi11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ALMI11"


class Alpa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ALPA3"


class Alpa4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ALPA4"


class Also3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ALSO3"


class Alup11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ALUP11"


class Alup3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ALUP3"


class Alup4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ALUP4"


class Alzr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ALZR11"


class Amar3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AMAR3"


class Amgn34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AMGN34"


class Amzo34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AMZO34"


class Ancr11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ANCR11B"


class Anim3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ANIM3"


class Anim3T(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ANIM3T"


class Aper3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "APER3"


class Aqll11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AQLL11"


class Arfi11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ARFI11B"


class Armt34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ARMT34"


class Arnc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ARNC34"


class Arzz3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ARZZ3"


class Atcr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ATCR11"


class Atom3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ATOM3"


class Atsa11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ATSA11B"


class Attb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ATTB34"


class Avon34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "AVON34"


class Axpb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AXPB34"


class Azev3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AZEV3"


class Azev4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AZEV4"


class Azul4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "AZUL4"


class B3Sa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "B3SA3"


class Bahi3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BAHI3"


class Balm3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BALM3"


class Balm4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BALM4"


class Bari11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BARI11"


class Bauh4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BAUH4"


class Baza3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BAZA3"


class Bbas3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BBAS3"


class Bbdc3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BBDC3"


class Bbdc4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BBDC4"


class Bbfi11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BBFI11B"


class Bbim11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BBIM11"


class Bbpo11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BBPO11"


class Bbrc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BBRC11"


class Bbrk3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BBRK3"


class Bbse3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BBSE3"


class Bbvj11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BBVJ11"


class Bbyy34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BBYY34"


class Bcff11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BCFF11"


class Bcia11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BCIA11"


class Bcri11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BCRI11"


class Bdll4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BDLL4"


class Beef11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BEEF11"


class Beef3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BEEF3"


class Bees3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BEES3"


class Bees4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BEES4"


class Berk34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BERK34"


class Bgip3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BGIP3"


class Bgip4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BGIP4"


class Bidi11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BIDI11"


class Bidi3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BIDI3"


class Bidi4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BIDI4"


class Bidi4T(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BIDI4T"


class Biib34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BIIB34"


class Biom3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BIOM3"


class Bkbr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BKBR3"


class Blak34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BLAK34"


class Bmeb3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BMEB3"


class Bmeb4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BMEB4"


class Bmgb11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BMGB11"


class Bmgb4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BMGB4"


class Bmii11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BMII11"


class Bmin3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BMIN3"


class Bmin4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BMIN4"


class Bmks3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BMKS3"


class Bmlc11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BMLC11B"


class Bmyb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BMYB34"


class Bnbr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BNBR3"


class Bnfs11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BNFS11"


class Boac34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BOAC34"


class Bobr4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BOBR4"


class Boei34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BOEI34"


class Bony34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BONY34"


class Boxp34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BOXP34"


class Bpac11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BPAC11"


class Bpac3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BPAC3"


class Bpac5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BPAC5"


class Bpan4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BPAN4"


class Bpff11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BPFF11"


class Bpha3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BPHA3"


class Bprp11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BPRP11"


class Brap3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRAP3"


class Brap4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRAP4"


class Brcr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRCR11"


class Brdt3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BRDT3"


class Brfs3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRFS3"


class Brge11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRGE11"


class Brge12(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRGE12"


class Brge6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRGE6"


class Brht11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BRHT11B"


class Briv3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRIV3"


class Briv4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRIV4"


class Brkm3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRKM3"


class Brkm5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRKM5"


class Brml3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BRML3"


class Brpr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRPR3"


class Brsr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRSR3"


class Brsr5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRSR5"


class Brsr6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BRSR6"


class Bsev3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BSEV3"


class Bsli4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BSLI4"


class Btc(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BTC"


class BtcUsd(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    capital_gains = models.FloatField(
        db_column="capital gains", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BTC-USD"


class Btcr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BTCR11"


class Btow3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BTOW3"


class Bttl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BTTL3"


class Bvar11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "BVAR11"


class Bvsp(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "BVSP"


class Camb10(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CAMB10"


class Camb4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CAMB4"


class Caml3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CAML3"


class Card3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CARD3"


class Care11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CARE11"


class Catp34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CATP34"


class Cbee3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CBEE3"


class Cbop11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CBOP11"


class Ccpr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CCPR3"


class Ccro3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CCRO3"


class Ccxc3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CCXC3"


class Cdi(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CDI"


class CdiOver(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CDI_OVER"


class Ceab3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CEAB3"


class Cebr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CEBR3"


class Cedo3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CEDO3"


class Cedo4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CEDO4"


class Ceeb3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CEEB3"


class Ceeb5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CEEB5"


class Ceed3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CEED3"


class Celp3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CELP3"


class Celp5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CELP5"


class Celp6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CELP6"


class Celp7(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CELP7"


class Ceoc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CEOC11"


class Cepe5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CEPE5"


class Cesp3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CESP3"


class Cesp5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CESP5"


class Cesp6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CESP6"


class Cgas3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CGAS3"


class Cgas5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CGAS5"


class Cgra3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CGRA3"


class Cgra4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CGRA4"


class Chke34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CHKE34"


class Chvx34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CHVX34"


class Ciel3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CIEL3"


class Clgn34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CLGN34"


class Clsc4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CLSC4"


class Cmcs34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CMCS34"


class Cmig3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CMIG3"


class Cmig4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CMIG4"


class Cnes11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CNES11"


class Cnto3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CNTO3"


class Coca34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "COCA34"


class Coce3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "COCE3"


class Coce5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "COCE5"


class Cogn3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "COGN3"


class Colg34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "COLG34"


class Coph34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "COPH34"


class Corr4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CORR4"


class Coty34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "COTY34"


class Cowc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "COWC34"


class Cpfe3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CPFE3"


class Cple3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CPLE3"


class Cple6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CPLE6"


class Cpre3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CPRE3"


class Cpre3T(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CPRE3T"


class Cpts11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CPTS11B"


class Crde3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CRDE3"


class Crfb3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CRFB3"


class Criv3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CRIV3"


class Criv4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CRIV4"


class Crpg5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CRPG5"


class Crpg6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CRPG6"


class Csan3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CSAN3"


class Csco34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CSCO34"


class Csmg3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CSMG3"


class Csna3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CSNA3"


class Csrn3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CSRN3"


class Ctgp34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CTGP34"


class Ctka4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CTKA4"


class Ctnm3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CTNM3"


class Ctnm4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CTNM4"


class Ctsa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CTSA3"


class Ctsa4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CTSA4"


class Ctsh34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CTSH34"


class Ctxt11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CTXT11"


class Cvbi11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CVBI11"


class Cvcb3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CVCB3"


class Cvcb3T(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "CVCB3T"


class Cvsh34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CVSH34"


class Cxce11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CXCE11B"


class Cxri11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CXRI11"


class Cxtl11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CXTL11"


class Cyre3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "CYRE3"


class Damt11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DAMT11B"


class Dasa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DASA3"


class Ddnb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DDNB34"


class Deai34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DEAI34"


class Desocupada(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "DESOCUPADA"


class Dher34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DHER34"


class Dirr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DIRR3"


class Disb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DISB34"


class Dmac11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DMAC11"


class Dmmo11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "DMMO11"


class Dmmo3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "DMMO3"


class Dmmo3T(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "DMMO3T"


class Dohl4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DOHL4"


class DolarCompra(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "DOLAR_COMPRA"


class DolarCompraMedia(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "DOLAR_COMPRA_MEDIA"


class DolarVenda(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "DOLAR_VENDA"


class DolarVendaMedia(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "DOLAR_VENDA_MEDIA"


class Domc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DOMC11"


class Dovl11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DOVL11B"


class Drit11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DRIT11B"


class Dtcy3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DTCY3"


class Dtex3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "DTEX3"


class Dukb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "DUKB34"


class Ealt3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EALT3"


class Ealt4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EALT4"


class Ebay34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EBAY34"


class Ecor3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ECOR3"


class Ecpr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ECPR3"


class Edfo11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EDFO11B"


class Edga11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EDGA11"


class Eeel3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "EEEL3"


class Eeel4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "EEEL4"


class Egie3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EGIE3"


class Ektr4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EKTR4"


class Eldo11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ELDO11B"


class Elek3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ELEK3"


class Elek4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ELEK4"


class Elet3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ELET3"


class Elet6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ELET6"


class Elpl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ELPL3"


class Emae4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EMAE4"


class Embr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EMBR3"


class Enat3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ENAT3"


class Enbr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ENBR3"


class Enev3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ENEV3"


class Engi11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ENGI11"


class Engi3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ENGI3"


class Engi4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ENGI4"


class Enma3B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ENMA3B"


class Enmt3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ENMT3"


class Enmt4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ENMT4"


class Eqtl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EQTL3"


class Erpa11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ERPA11"


class Estr4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ESTR4"


class Esud11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ESUD11"


class Esut11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ESUT11"


class Eter3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ETER3"


class EtfList(models.Model):
    razão_social = models.TextField(
        db_column="Razão Social", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fundo = models.TextField(
        db_column="Fundo", blank=True, null=True
    )  # Field name made lowercase.
    segmento = models.FloatField(
        db_column="Segmento", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ETF_LIST"


class Euca4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EUCA4"


class Euro11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EURO11"


class EuroCompra(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "EURO_COMPRA"


class EuroVenda(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "EURO_VENDA"


class Even3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EVEN3"


class Exportacoes(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "EXPORTACOES"


class Exxo34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EXXO34"


class Eztc3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "EZTC3"


class Faed11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FAED11"


class Famb11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FAMB11B"


class Fbok34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "FBOK34"


class Fcfl11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FCFL11"


class Fcxo34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FCXO34"


class Fdmo34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FDMO34"


class Fdxb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FDXB34"


class Fesa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FESA3"


class Fesa4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FESA4"


class Fexc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "FEXC11"


class Fher3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FHER3"


class Figs11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FIGS11"


class Fiib11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FIIB11"


class Fiip11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FIIP11B"


class FiiList(models.Model):
    symbol = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "FII_LIST"


class Finf11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "FINF11"


class Fisc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FISC11"


class Fisd11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "FISD11"


class Fivn11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FIVN11"


class Fixx11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FIXX11"


class Flma11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FLMA11"


class Flrp11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FLRP11"


class Flry3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FLRY3"


class Fmof11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FMOF11"


class Fmxb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FMXB34"


class Fnam11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FNAM11"


class Fnor11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FNOR11"


class Foft11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FOFT11"


class ForcaDeTrabalho(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "FORCA_DE_TRABALHO"


class Fpab11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FPAB11"


class Fpng11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FPNG11"


class Fras3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FRAS3"


class Frio3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FRIO3"


class Frta3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FRTA3"


class Fslr34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FSLR34"


class Fspe11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FSPE11"


class Fsrf11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FSRF11"


class Fstu11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FSTU11"


class Ftce11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FTCE11B"


class Fvbi11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "FVBI11"


class Fvpq11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "FVPQ11"


class Gbio33(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "GBIO33"


class Gdbr34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GDBR34"


class Geoo34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GEOO34"


class Gepa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GEPA3"


class Gepa4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GEPA4"


class Gese11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GESE11B"


class Gfsa1(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "GFSA1"


class Gfsa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GFSA3"


class Ggbr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GGBR3"


class Ggbr4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GGBR4"


class Ggrc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GGRC11"


class Gild34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GILD34"


class Gmco34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GMCO34"


class Gndi3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "GNDI3"


class Goau3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GOAU3"


class Goau4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GOAU4"


class Gogl34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GOGL34"


class Gogl35(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GOGL35"


class Goll4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GOLL4"


class Gpar3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GPAR3"


class Gpcp3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "GPCP3"


class Gpiv33(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GPIV33"


class Gpro34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GPRO34"


class Gpsi34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GPSI34"


class Grlv11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GRLV11"


class Grnd3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GRND3"


class Gsgi34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GSGI34"


class Gshp3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GSHP3"


class Gtwr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GTWR11"


class Guar3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "GUAR3"


class Habt11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HABT11"


class Haga3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HAGA3"


class Haga4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HAGA4"


class Hali34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HALI34"


class Hapv3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HAPV3"


class Hbor3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HBOR3"


class Hbts5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HBTS5"


class Hbtt11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "HBTT11"


class Hcri11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HCRI11"


class Hctr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HCTR11"


class Heta4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HETA4"


class Hfof11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HFOF11"


class Hgbs11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HGBS11"


class Hgcr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HGCR11"


class Hgff11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HGFF11"


class Hglg11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HGLG11"


class Hgpo11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HGPO11"


class Hgre11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HGRE11"


class Hgru11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HGRU11"


class Hgtx3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "HGTX3"


class Hmoc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HMOC11"


class Home34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HOME34"


class Honb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HONB34"


class Hoot4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HOOT4"


class Hpqb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HPQB34"


class Hrdf11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HRDF11"


class Hshy34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HSHY34"


class Hsml11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HSML11"


class Htmx11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HTMX11"


class Husc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HUSC11"


class Hype3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "HYPE3"


class Ibff11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "IBFF11"


class Ibmb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "IBMB34"


class Ibov(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IBOV"


class Ibra(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IBRA"


class Ibxl(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IBXL"


class Ibxx(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IBXX"


class Ico2(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "ICO2"


class Icon(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "ICON"


class Idiv(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IDIV"


class Idnt3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "IDNT3"


class Idvl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "IDVL3"


class Idvl4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "IDVL4"


class Idvl9(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "IDVL9"


class Ieex(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IEEX"


class Ifil(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IFIL"


class Ifix(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IFIX"


class Ifnc(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IFNC"


class Igbr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "IGBR3"


class Igct(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IGCT"


class Igcx(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IGCX"


class Ignm(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IGNM"


class Igpm(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "IGPM"


class Igta3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "IGTA3"


class Imat(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IMAT"


class Imob(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IMOB"


class Importacoes(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "IMPORTACOES"


class Industria(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "INDUSTRIA"


class Indx(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "INDX"


class Inep3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "INEP3"


class Inep4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "INEP4"


class Inpc(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "INPC"


class Ipca(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "IPCA"


class Ipca15(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "IPCA_15"


class Irbr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "IRBR3"


class Irdm11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "IRDM11"


class Itag(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "ITAG"


class Itec3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ITEC3"


class Itlc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ITLC34"


class Itsa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ITSA3"


class Itsa4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ITSA4"


class Itub3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ITUB3"


class Itub4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ITUB4"


class Ivbx(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "IVBX"


class Jbdu1(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "JBDU1"


class Jbdu2(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "JBDU2"


class Jbdu3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "JBDU3"


class Jbdu4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "JBDU4"


class Jbss3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "JBSS3"


class Jcpc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "JCPC34"


class Jfen3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "JFEN3"


class Jhsf3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "JHSF3"


class Jnjb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "JNJB34"


class Jopa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "JOPA3"


class Jopa4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "JOPA4"


class Jpmc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "JPMC34"


class Jppc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "JPPC11"


class Jpsa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "JPSA3"


class Jrdm11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "JRDM11"


class Jslg3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "JSLG3"


class Jsre11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "JSRE11"


class Kepl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KEPL3"


class Khcb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KHCB34"


class Kinp11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KINP11"


class Klbn11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KLBN11"


class Klbn3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KLBN3"


class Klbn4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KLBN4"


class Kmbb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KMBB34"


class Kncr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KNCR11"


class Knhy11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KNHY11"


class Knip11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KNIP11"


class Knre11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KNRE11"


class Knri11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "KNRI11"


class Lame3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "LAME3"


class Lame4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "LAME4"


class Latr11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LATR11B"


class Lbrn34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "LBRN34"


class Lcam3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "LCAM3"


class Leve3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LEVE3"


class Ligt3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LIGT3"


class Lily34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LILY34"


class Linx3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "LINX3"


class Lipr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LIPR3"


class Liqo3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "LIQO3"


class Llis3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "LLIS3"


class Lmtb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LMTB34"


class Logg3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LOGG3"


class Logn12(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "LOGN12"


class Logn3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LOGN3"


class Lpsb3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LPSB3"


class Lren3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LREN3"


class Lupa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LUPA3"


class Luxm4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "LUXM4"


class Macy34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MACY34"


class Mapt3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MAPT3"


class MassaSaraial(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "MASSA_SARAIAL"


class Maxr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MAXR11"


class Mbrf11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MBRF11"


class Mcdc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MCDC34"


class Mdia3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MDIA3"


class Mdlz34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MDLZ34"


class Mdtc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MDTC34"


class Meal3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MEAL3"


class Meli34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MELI34"


class Mend5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "MEND5"


class Mend6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "MEND6"


class Merc4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MERC4"


class Metb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "METB34"


class Mfii11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MFII11"


class Mgel4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MGEL4"


class Mgff11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MGFF11"


class Mglu3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MGLU3"


class Mils3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MILS3"


class Mlcx(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "MLCX"


class Mmmc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MMMC34"


class Mmxm11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MMXM11"


class Mmxm3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "MMXM3"


class Mndl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MNDL3"


class Mnpr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MNPR3"


class Moar3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MOAR3"


class Mosc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MOSC34"


class Movi3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MOVI3"


class Mrck34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MRCK34"


class Mrfg3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MRFG3"


class Mrsa3B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MRSA3B"


class Mrsa6Bf(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MRSA6BF"


class Mrve3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MRVE3"


class Msbr34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MSBR34"


class Mscd34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MSCD34"


class Msft34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MSFT34"


class Mspa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MSPA3"


class Mtig4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "MTIG4"


class Mtsa4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MTSA4"


class Mult3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MULT3"


class Mwet4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MWET4"


class Mxrf11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MXRF11"


class Mypk12(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "MYPK12"


class Mypk3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "MYPK3"


class Nasdaq(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "NASDAQ"


class Natu3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "NATU3"


class Nchb11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "NCHB11"


class Neoe3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "NEOE3"


class Nflx34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "NFLX34"


class Nike34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "NIKE34"


class Npar11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "NPAR11"


class Nslu11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "NSLU11"


class Nutr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "NUTR3"


class Nvho11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "NVHO11"


class Nvif11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "NVIF11B"


class Ocupadas(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "OCUPADAS"


class Odpv3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ODPV3"


class Ofsa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "OFSA3"


class Oibr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "OIBR3"


class Oibr4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "OIBR4"


class Omge3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "OMGE3"


class Onef11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ONEF11"


class Orcl34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ORCL34"


class Orpd11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ORPD11"


class Osxb3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "OSXB3"


class Oucy11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "OUCY11"


class Oujp11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "OUJP11"


class Oulg11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "OULG11B"


class OuroCompra(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "OURO_COMPRA"


class OuroVenda(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "OURO_VENDA"


class Paby11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PABY11"


class Pard3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PARD3"


class Patc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PATC11"


class Pati3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PATI3"


class Pati4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PATI4"


class Pblv11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "PBLV11"


class Pcar4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "PCAR4"


class Pdgr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PDGR3"


class Peab3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PEAB3"


class Peab4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PEAB4"


class Pepb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PEPB34"


class Petr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PETR3"


class Petr4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PETR4"


class Pfiz34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PFIZ34"


class Pfrm3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PFRM3"


class Pgco34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PGCO34"


class Pine4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PINE4"


class Pip(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "PIP"


class Plas3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PLAS3"


class Plri11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PLRI11"


class Pmam3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PMAM3"


class Pnvl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PNVL3"


class Pnvl4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "PNVL4"


class Pomo10(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "POMO10"


class Pomo3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "POMO3"


class Pomo4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "POMO4"


class PopulacaoEmIdadeAtiva(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "POPULACAO_EM_IDADE_ATIVA"


class Pord11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PORD11"


class Posi3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "POSI3"


class Poupanca(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "POUPANCA"


class Ppla11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PPLA11"


class Pqdp11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PQDP11"


class Prio3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PRIO3"


class Prsn11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PRSN11B"


class Prsv11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PRSV11"


class Prts11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "PRTS11"


class Pssa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PSSA3"


class Ptbl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PTBL3"


class Ptnt4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "PTNT4"


class Qcom34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "QCOM34"


class Qual3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "QUAL3"


class Radl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RADL3"


class Rail3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RAIL3"


class Rani3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RANI3"


class Rani4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "RANI4"


class Rapt3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RAPT3"


class Rapt4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RAPT4"


class Rbbv11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBBV11"


class Rbcb11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBCB11"


class Rbco11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBCO11"


class Rbds11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBDS11"


class Rbed11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBED11"


class Rbff11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBFF11"


class Rbgs11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBGS11"


class Rbrd11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBRD11"


class Rbrf11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBRF11"


class Rbrp11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBRP11"


class Rbrr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBRR11"


class Rbry11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBRY11"


class Rbva11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBVA11"


class Rbvo11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RBVO11"


class Rcfa11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RCFA11"


class Rcrb11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RCRB11"


class Rcri11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RCRI11B"


class Rcsl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RCSL3"


class Rcsl4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RCSL4"


class Rdes11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RDES11"


class Rdni3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RDNI3"


class Rdpd11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RDPD11"


class Rect11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RECT11"


class Rede3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "REDE3"


class Reit11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "REIT11"


class RemuneracaoMediaNominal(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "REMUNERACAO_MEDIA_NOMINAL"


class Rent3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RENT3"


class ResevasInternacionais(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "RESEVAS_INTERNACIONAIS"


class Rigg34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RIGG34"


class Rlog3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "RLOG3"


class Rndp11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RNDP11"


class Rnew11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RNEW11"


class Rnew3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RNEW3"


class Rnew4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RNEW4"


class Rngo11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RNGO11"


class Romi3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ROMI3"


class Rost34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ROST34"


class Rpad3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RPAD3"


class Rpad5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RPAD5"


class Rpad6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RPAD6"


class Rpmg3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RPMG3"


class Rsid3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RSID3"


class Rspd11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RSPD11"


class Rsul4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "RSUL4"


class Saag11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SAAG11"


class Sadi11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SADI11"


class Saic11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SAIC11B"


class Sanb11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SANB11"


class Sanb3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SANB3"


class Sanb4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SANB4"


class Sanc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    capital_gains = models.FloatField(
        db_column="capital gains", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SANC34"


class Sapr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SAPR11"


class Sapr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SAPR3"


class Sapr4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SAPR4"


class Sbsp3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SBSP3"


class Sbub34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SBUB34"


class Scar3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SCAR3"


class Schw34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SCHW34"


class Scpf11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SCPF11"


class Sdil11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SDIL11"


class Sdip11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SDIP11"


class Sedu3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SEDU3"


class Seer3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SEER3"


class Seer3T(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SEER3T"


class Selic(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SELIC"


class SelicMeta(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SELIC_META"


class Servicos(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SERVICOS"


class Sfnd11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SFND11"


class Sgps3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SGPS3"


class Shdp11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SHDP11B"


class Shop11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SHOP11"


class Show3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SHOW3"


class Shph11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SHPH11"


class Shul4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SHUL4"


class Slbg34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SLBG34"


class Slce3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SLCE3"


class Sled3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SLED3"


class Sled4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SLED4"


class Smal11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SMAL11"


class Smll(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "SMLL"


class Smls3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SMLS3"


class Smls3T(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SMLS3T"


class Smto3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SMTO3"


class Snsy5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SNSY5"


class Sond5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SOND5"


class Sond6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SOND6"


class Sp500(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SP500"


class Spaf11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SPAF11"


class Spri3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SPRI3"


class Sprn34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SPRN34"


class Sptw11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SPTW11"


class Sqia3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SQIA3"


class Ssfo34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SSFO34"


class Stbp3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "STBP3"


class StockList(models.Model):
    symbol = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    isin = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "STOCK_LIST"


class Strx11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "STRX11"


class Sula11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SULA11"


class Sula3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SULA3"


class Sula4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SULA4"


class Suzb3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "SUZB3"


class Taee11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TAEE11"


class Taee3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TAEE3"


class Taee4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TAEE4"


class Tasa13(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TASA13"


class Tasa15(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TASA15"


class Tasa17(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TASA17"


class Tasa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TASA3"


class Tasa4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TASA4"


class TaxaDeDesocupacao(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TAXA_DE_DESOCUPACAO"


class Tbof11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TBOF11"


class Tcno3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TCNO3"


class Tcno4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TCNO4"


class Tcpf11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TCPF11"


class Tcr11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TCR11"


class Tcsa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TCSA3"


class Tecn3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TECN3"


class Teka4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TEKA4"


class Telb3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TELB3"


class Telb4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TELB4"


class Tend3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TEND3"


class Tesa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TESA3"


class Texa34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TEXA34"


class Tfof11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TFOF11"


class Tgar11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TGAR11"


class Tgma3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TGMA3"


class Tgtb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TGTB34"


class Thra11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "THRA11"


class Tiet11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TIET11"


class Tiet2(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TIET2"


class Tiet3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TIET3"


class Tiet4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TIET4"


class Tiff34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TIFF34"


class Timp3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TIMP3"


class Tmos34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TMOS34"


class Torm13(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TORM13"


class Tots3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TOTS3"


class Tour11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TOUR11"


class Toyb3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TOYB3"


class Toyb4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TOYB4"


class Tpis3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TPIS3"


class Tris3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TRIS3"


class Trnt11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TRNT11"


class Trpl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TRPL3"


class Trpl4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TRPL4"


class Trpn3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TRPN3"


class Trvc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TRVC34"


class Trxl11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TRXL11"


class Tsla34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TSLA34"


class Tsnc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TSNC11"


class Tupy3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TUPY3"


class Twtr34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "TWTR34"


class Txrx4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "TXRX4"


class TesouroIgpmComJurosSemestrais(models.Model):
    data_vencimento = models.DateField(
        db_column="Data Vencimento", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_base = models.DateField(
        db_column="Data Base", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_compra_manha = models.FloatField(
        db_column="Taxa Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_venda_manha = models.FloatField(
        db_column="Taxa Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_compra_manha = models.FloatField(
        db_column="PU Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_venda_manha = models.FloatField(
        db_column="PU Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_base_manha = models.FloatField(
        db_column="PU Base Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "Tesouro IGPM+ com Juros Semestrais"


class TesouroIpca(models.Model):
    data_vencimento = models.DateField(
        db_column="Data Vencimento", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_base = models.DateField(
        db_column="Data Base", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_compra_manha = models.FloatField(
        db_column="Taxa Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_venda_manha = models.FloatField(
        db_column="Taxa Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_compra_manha = models.FloatField(
        db_column="PU Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_venda_manha = models.FloatField(
        db_column="PU Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_base_manha = models.FloatField(
        db_column="PU Base Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "Tesouro IPCA+"


class TesouroIpcaComJurosSemestrais(models.Model):
    data_vencimento = models.DateField(
        db_column="Data Vencimento", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_base = models.DateField(
        db_column="Data Base", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_compra_manha = models.FloatField(
        db_column="Taxa Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_venda_manha = models.FloatField(
        db_column="Taxa Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_compra_manha = models.FloatField(
        db_column="PU Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_venda_manha = models.FloatField(
        db_column="PU Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_base_manha = models.FloatField(
        db_column="PU Base Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "Tesouro IPCA+ com Juros Semestrais"


class TesouroPrefixado(models.Model):
    data_vencimento = models.DateField(
        db_column="Data Vencimento", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_base = models.DateField(
        db_column="Data Base", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_compra_manha = models.FloatField(
        db_column="Taxa Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_venda_manha = models.FloatField(
        db_column="Taxa Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_compra_manha = models.FloatField(
        db_column="PU Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_venda_manha = models.FloatField(
        db_column="PU Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_base_manha = models.FloatField(
        db_column="PU Base Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "Tesouro Prefixado"


class TesouroPrefixadoComJurosSemestrais(models.Model):
    data_vencimento = models.DateField(
        db_column="Data Vencimento", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_base = models.DateField(
        db_column="Data Base", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_compra_manha = models.FloatField(
        db_column="Taxa Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_venda_manha = models.FloatField(
        db_column="Taxa Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_compra_manha = models.FloatField(
        db_column="PU Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_venda_manha = models.FloatField(
        db_column="PU Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_base_manha = models.FloatField(
        db_column="PU Base Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "Tesouro Prefixado com Juros Semestrais"


class TesouroRendaAposentadoriaExtra(models.Model):
    data_vencimento = models.DateField(
        db_column="Data Vencimento", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_base = models.DateField(
        db_column="Data Base", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_compra_manha = models.FloatField(
        db_column="Taxa Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_venda_manha = models.FloatField(
        db_column="Taxa Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_compra_manha = models.FloatField(
        db_column="PU Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_venda_manha = models.FloatField(
        db_column="PU Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_base_manha = models.FloatField(
        db_column="PU Base Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "Tesouro Renda+ Aposentadoria Extra"


class TesouroSelic(models.Model):
    data_vencimento = models.DateField(
        db_column="Data Vencimento", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_base = models.DateField(
        db_column="Data Base", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_compra_manha = models.FloatField(
        db_column="Taxa Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_venda_manha = models.FloatField(
        db_column="Taxa Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_compra_manha = models.FloatField(
        db_column="PU Compra Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_venda_manha = models.FloatField(
        db_column="PU Venda Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pu_base_manha = models.FloatField(
        db_column="PU Base Manha", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "Tesouro Selic"


class Ubsg34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "UBSG34"


class Ucas3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "UCAS3"


class Ugpa3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "UGPA3"


class Unip3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "UNIP3"


class Unip5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "UNIP5"


class Unip6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "UNIP6"


class Upac34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "UPAC34"


class Upss34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "UPSS34"


class Usbc34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "USBC34"


class Usd(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "USD"


class Usim3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "USIM3"


class Usim5(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "USIM5"


class Usim6(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "USIM6"


class Ussx34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "USSX34"


class Utec34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "UTEC34"


class Util(models.Model):
    setor = models.TextField(
        db_column="Setor", blank=True, null=True
    )  # Field name made lowercase.
    código = models.TextField(
        db_column="Código", primary_key=True
    )  # Field name made lowercase.
    ação = models.TextField(
        db_column="Ação", blank=True, null=True
    )  # Field name made lowercase.
    tipo = models.TextField(
        db_column="Tipo", blank=True, null=True
    )  # Field name made lowercase.
    qtde_teórica = models.BigIntegerField(
        db_column="Qtde. Teórica", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_field = models.FloatField(
        db_column="Part", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_acum_field = models.FloatField(
        db_column="PartAcum.", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "UTIL"


class Vale3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VALE3"


class Vamo3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VAMO3"


class Vere11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VERE11"


class Verz34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VERZ34"


class Vgir11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VGIR11"


class Vilg11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VILG11"


class Visa34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VISA34"


class Visc11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VISC11"


class Viva3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VIVA3"


class Vivr3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VIVR3"


class Vivt3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VIVT3"


class Vivt4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "VIVT4"


class Vlid3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VLID3"


class Vljs11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "VLJS11"


class Vloe34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VLOE34"


class Vlol11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VLOL11"


class Vpsi11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "VPSI11"


class Vrta11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VRTA11"


class Vsho11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VSHO11"


class Vspt3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    capital_gains = models.FloatField(
        db_column="capital gains", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VSPT3"


class Vtlt11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VTLT11"


class Vulc3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "VULC3"


class Vvar3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "VVAR3"


class Walm34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "WALM34"


class Wege3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "WEGE3"


class Wfco34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "WFCO34"


class Whrl3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "WHRL3"


class Whrl4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "WHRL4"


class Wizs3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "WIZS3"


class Wlmm3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "WLMM3"


class Wlmm4(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "WLMM4"


class Wplz11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "WPLZ11"


class Wplz11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "WPLZ11B"


class Wson33(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "WSON33"


class Wtsp11B(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "WTSP11B"


class Wuni34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "WUNI34"


class Xfix11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "XFIX11"


class Xfix11Sa(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "XFIX11.SA"


class Xpcm11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "XPCM11"


class Xpht11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "XPHT11"


class Xpht12(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "XPHT12"


class Xpin11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "XPIN11"


class Xplg11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "XPLG11"


class Xpom11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "XPOM11"


class Xrxb34(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "XRXB34"


class Xted11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "XTED11"


class Ychy11(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "YCHY11"


class Yduq3(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "YDUQ3"


class Dollar(models.Model):
    date = models.DateTimeField(
        primary_key=True,
    )
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    dividends = models.IntegerField(blank=True, null=True)
    stock_splits = models.IntegerField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "dollar"


class Fiis(models.Model):
    symbol = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fiis"


class Ibovespa(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    dividends = models.IntegerField(blank=True, null=True)
    stock_splits = models.IntegerField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "ibovespa"


class Smal(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    dividends = models.IntegerField(blank=True, null=True)
    stock_splits = models.IntegerField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "smal"


class StocksBr(models.Model):
    symbol = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    isin = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "stocks_br"


class Symbol(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(
        db_column="adj close", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "symbol"


class Xfix(models.Model):
    date = models.DateTimeField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    dividends = models.FloatField(blank=True, null=True)
    stock_splits = models.FloatField(
        db_column="stock splits", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "xfix"
