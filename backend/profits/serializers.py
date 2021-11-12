from datetime import date
from django.db import models
from rest_framework import serializers
from profits.models import Trade


class TradeListSerializer(serializers.ListSerializer):

    # def daytrades(self, obj):
    #     trades = {}
    #     for trade in obj:
    #         if trade["data"] in trades.keys():
    #             trades[trade["data"]].append(trade)
    #         else:
    #             trades[trade["data"]] = [
    #                 trade,
    #             ]
    #     for trade in trades.values():
    #         ativos_unicos = [daytrade['ativo'] for daytrade in]
    #     return trades

    def create(self, validated_data):
        trades = [Trade(**trade) for trade in validated_data]
        # test = self.daytrades(validated_data)
        # print(test)
        return Trade.objects.bulk_create(trades)


class TradeSerializer(serializers.ModelSerializer):
    daytrade = serializers.SerializerMethodField()
    # preco_medio = serializers.SerializerMethodField()
    # quantidade_acumulada = serializers.SerializerMethodField()
    # lucro = serializers.SerializerMethodField()

    def get_daytrade(self, obj):
        try:
            trades = Trade.objects.filter(ativo=obj.ativo, data=obj.data)
        except Exception as err:
            raise Exception(err)
        else:
            if obj.operacao == "VENDA":
                return len(trades.filter(operacao="COMPRA")) > 0
            else:
                return len(trades.filter(operacao="VENDA")) > 0

    class Meta:
        model = Trade
        list_serializer_class = TradeListSerializer
        exclude = ("id",)

    def create(self, validated_data):
        return super().create(validated_data)

    # def get_preco_medio(self, obj):
    #     if obj.operacao == "VENDA":
    #         return None
    #     else:
    #         actual_mean_price = obj.preco + (obj.custos / obj.quantidade)
    #         try:
    #             last_buy = Trade.objects.filter(ativo=obj.ativo, operacao="COMPRA")[-1]
    #         except Exception as err:
    #             print(err)
    #             return actual_mean_price
    #         else:
    #             return (actual_mean_price + last_buy.preco_medio) / 2

    # def get_quantidade_acumulada(self, obj):
    #     try:
    #         trades = Trade.objects.filter(ativo=obj.ativo, data__lte=obj.data)
    #     except Exception as err:
    #         raise Exception(err)
    #     else:
    #         pre_total = sum(
    #             [
    #                 trade.quantidade
    #                 if trade.operacao == "COMPRA"
    #                 else -trade.quantidade
    #                 for trade in trades
    #             ]
    #         )
    #         pos_total = (
    #             pre_total + obj.quantidade
    #             if obj.operacao == "COMPRA"
    #             else pre_total - obj.quantidade
    #         )
    #         print(
    #             f"\npre_total: {pre_total}\ntotal: {obj.quantidade}\npos_total: {pos_total}"
    #         )
    #         return pos_total

    # def lucro(self, obj):
    #     if obj.operacao == "COMPRA":
    #         return None
    #     else:
    #         sell_price = (obj.quantidade * obj.preco) - obj.custos
    #         last_buy = Trade.objects.filter(ativo=obj.ativo, operacao="COMPRA")[-1]
    #         return sell_price - (last_buy.quantidade_acumulada * last_buy.preco_medio)
