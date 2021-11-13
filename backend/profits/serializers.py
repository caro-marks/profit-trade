from rest_framework import serializers
from profits.models import Trade


class TradeListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        trades = [Trade(**trade) for trade in validated_data]
        return Trade.objects.bulk_create(trades)


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        list_serializer_class = TradeListSerializer
        exclude = ("id",)

    def create(self, validated_data):
        return super().create(validated_data)

    daytrade = serializers.SerializerMethodField()
    preco_medio = serializers.SerializerMethodField()
    # quantidade_acumulada = serializers.SerializerMethodField()
    # lucro = serializers.SerializerMethodField()

    def get_daytrade(self, obj):
        # print(f'\n{Trade.objects.all()}\n')
        # print(obj.ativo, obj.data, obj.operacao)
        try:
            trades = Trade.objects.filter(ativo=obj.ativo, data=obj.data)
        except Exception as err:
            raise Exception(err)
        else:
            if obj.operacao == "VENDA":
                return len(trades.filter(operacao="COMPRA")) > 0
            else:
                return len(trades.filter(operacao="VENDA")) > 0

    def get_preco_medio(self, obj):
        if obj.operacao == "VENDA":
            return None
        else:
            actual_mean_price = obj.preco + (obj.custos / obj.quantidade)
            try:
                last_buy = Trade.objects.filter(
                    ativo=obj.ativo, operacao="COMPRA", data__lt=obj.data
                ).last()
            except Exception as err:
                print(err)
            else:
                print('\n', obj.ativo, obj.operacao, obj.data)
                if last_buy:
                    print(last_buy.ativo, last_buy.operacao, last_buy.data, '\n')
                    latest_mean_price = last_buy.preco + (
                        last_buy.custos / last_buy.quantidade
                    )
                    return (actual_mean_price + latest_mean_price) / 2
                else:
                    print(f'{last_buy} \n')
                    return actual_mean_price

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
