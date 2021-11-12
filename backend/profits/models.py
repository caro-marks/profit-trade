from django.db import models
from django.utils import timezone


# class Asset(models.Model):

#     name = models.CharField(max_length=128)

#     def __str__(self):
#         return f"ativo: {self.name}"


class Trade(models.Model):

    OPERATIONS_CHOICES = (("COMPRA", "BUY"), ("VENDA", "SELL"))

    ativo = models.CharField(max_length=128, default=None)
    operacao = models.CharField(choices=OPERATIONS_CHOICES, max_length=6)
    data = models.DateField(default=timezone.now)
    quantidade = models.PositiveSmallIntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    custos = models.DecimalField(max_digits=4, decimal_places=2)
    daytrade = models.BooleanField(default=False)
    preco_medio = models.DecimalField(
        max_digits=8, decimal_places=2, default=None, null=True
    )
    quantidade_acumulada = models.PositiveSmallIntegerField(default=0)
    lucro = models.DecimalField(max_digits=8, decimal_places=2, default=None, null=True)
