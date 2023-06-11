from rest_framework import serializers
from .models import Order
from stock.serializers import StockSerializer

class OrderSerializer(serializers.ModelSerializer):
    product=StockSerializer()
    class Meta:
        model=Order
        fields='__all__'