from rest_framework import serializers
from .models import Watchlist
from stock.serializers import StockSerializer

class WatchlistSerializer(serializers.ModelSerializer):
    product=StockSerializer()
    class Meta:
        model=Watchlist
        fields='__all__'