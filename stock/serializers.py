from rest_framework import serializers
from .models import Stock
from trader.serializers import TraderSerializer
from category.serializers import CategorySerializer
from design.serializers import DesignSerilaizer

class StockSerializer(serializers.ModelSerializer):
    artist=TraderSerializer()
    cat=CategorySerializer()
    design=DesignSerilaizer()
    class Meta:
        model=Stock
        ordering = ['-created']
        fields='__all__'