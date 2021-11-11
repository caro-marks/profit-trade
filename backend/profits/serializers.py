from datetime import date
from django.db import models
from rest_framework import serializers
from profits.models import Trade


class TradeSerializer(serializers.ModelSerializer):
    # daytrade = serializers.SerializerMethodField()
    # mean_price = serializers.SerializerMethodField()
    # total_quantity = serializers.SerializerMethodField()
    # profit = serializers.SerializerMethodField()
    print("serializer")

    class Meta:
        model = Trade
        fields = "__all__"

    # def get_daytrade(self, data):
    #     try:
    #         trades = Trade.objects.filter(asset=data.asset, date=data.date)
    #     except Exception as err:
    #         raise Exception(err)
    #     else:

    #         return len() != 0

    # def get_mean_price(self, data):
    #     return data.price + (data.costs / data.quantity)

    # def get_total_quantity(self, data):
    #     try:
    #         asset = Asset.objects.get(name=data.asset)
    #     except Exception as err:
    #         raise Exception(err)
