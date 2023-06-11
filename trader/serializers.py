from rest_framework import serializers
from .models import Trader
from account.serializers import CustomerSerializer

class TraderSerializer(serializers.ModelSerializer):
    cust=CustomerSerializer()
    class Meta:
        model=Trader
        fields='__all__'