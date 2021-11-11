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
    # daytrade = models.BooleanField()
    # mean_price = models.DecimalField(max_digits=8, decimal_places=2)
    # total_quantity = models.PositiveSmallIntegerField()
    # profit = models.DecimalField(max_digits=8, decimal_places=2)
