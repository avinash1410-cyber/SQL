from rest_framework import serializers
from .models import Stock
from trader.serializers import TraderSerializer
from category.serializers import CategorySerializer
from design.serializers import DesignSerilaizer

# class StockSerializer(serializers.ModelSerializer):
#     customer=TraderSerializer()
#     cat=CategorySerializer()
#     design=DesignSerilaizer()
#     class Meta:
#         model=Stock
#         ordering = ['-created']
#         fields='__all__'


class MarketSerializer(serializers.Serializer):
    symbol = serializers.CharField()
    price = serializers.FloatField()




class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'name', 'price', 'market_cap']