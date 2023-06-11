# Create your views here.
from rest_framework.views import APIView

from stock.models import Stock
from stock.serializers import StockSerializer
from .models import Design
from rest_framework.response import Response
from .serializers import DesignSerilaizer
class DesignsAPIView(APIView):
    def get(self,request,pk=None):
        if pk:
            design=Design.objects.get(id=pk)
            data=DesignSerilaizer(design)
            return Response(data.data)
        designs=Design.objects.all()
        data=DesignSerilaizer(designs,many=True)
        return Response(data.data)

class DesignProductsAPIView(APIView):
    def get(self,request,pk=None):
        if pk:
            design=Design.objects.get(id=pk)
            products=Stock.objects.filter(design=design)
            data=StockSerializer(products,many=True)
            return Response(data.data)