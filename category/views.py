from rest_framework.response import Response
from stock.models import Stock
from .models import Categories
from rest_framework.views import APIView
from .serializers import CategorySerializer
from stock.serializers import StockSerializer


# Create your views here.
class CategoryAPIView(APIView):
    def get(self,request,pk=None):
        if pk is None:
            products=Stock.objects.all()       
        else:
            cat = Categories.objects.get(id=pk)
            print(cat)
            products=Stock.objects.filter(cat=cat)             
        serializer=StockSerializer(products,many=True)
        return Response(serializer.data)

class AvailableCategory(APIView):
    def get(self,request):
        cat = Categories.objects.all()
        serializer=CategorySerializer(cat,many=True)
        return Response(serializer.data)