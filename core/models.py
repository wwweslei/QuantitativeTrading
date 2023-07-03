from django.contrib.auth import models as auth_models
from django.db import models

type_choices = [
    ("Fii", "Fundos imobiliários"),
    ("Stock", "Ações"),
    ("Crypto", "Criptomoedas"),
    ("Treasury", "Tesouro direto"),
    ("Etf", "exchange-traded fund"),
    ("BDR", "Brazilian Depositary Receipt"),
    ("RF", "Renda Fixa"),
]


class PortifolioUser(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        auth_models.User, related_name="userprofile", on_delete=models.CASCADE
    )
    type = models.CharField(choices=type_choices)
    cod = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Portifolio {self.user} - {self.type}"

    class Meta:
        managed = True
        db_table = "PortifolioUser"
