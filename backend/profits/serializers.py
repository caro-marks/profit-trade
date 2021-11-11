from django.db import models
from rest_framework import serializers
from profits.models import Trade


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        exclude = ('daytrade','mean_price','profit')

    daytrade = serializers.SerializerMethodField()
    mean_price = serializers.SerializerMethodField()
    profit = serializers.SerializerMethodField()