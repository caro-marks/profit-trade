from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DecimalField


class Asset(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return f"ativo: {self.name}"


class Trade(models.Model):

    OPERATIONS_CHOICES = (("BUY", "COMPRA"), ("SELL", "VENDA"))

    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)
    operation = models.CharField(choices=OPERATIONS_CHOICES, max_length=4)
    date = models.DateField(auto_now_add=True)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    costs = models.DecimalField(max_digits=4, decimal_places=2)
    daytrade = models.BooleanField()
    mean_price = DecimalField(max_digits=8, decimal_places=2)
    profit = models.DecimalField(max_digits=8, decimal_places=2)
