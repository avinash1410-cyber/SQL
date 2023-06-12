from rest_framework.views import APIView
from .models import Stock
from .serializers import StockSerializer
from rest_framework.response import Response
from django.db.models import Q
from cloudinary.forms import cl_init_js_callbacks      
from rest_framework.decorators import api_view, permission_classes



class StockSearchAPIView(APIView):
    def get(self,request,query=None):
        print("PRINTING THE SLUG",query)
        stocks=Stock.objects.filter(
                              Q(name__icontains=query))
        data=StockSerializer(stocks,many=True)
        return Response(data.data)



class Home(APIView):
    def get(self,*args,**kwargs):
        data = Stock.objects.all()
        serializer = StockSerializer(data,many=True)
        return Response(serializer.data)


class StockAPIView(APIView):
   # permission_classes=[IsAuthenticated]
    def get(self, request, pk=None, format=None):
        data = Stock.objects.get(id=pk)
        if data is None:
            return Response({"message":"Not valid id"})
        serializer = StockSerializer(data)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def StockMonthlyAPIView(self, request, pk=None, format=None):
    data = Stock.objects.get(id=pk)
    if data is None:
        return Response({"message":"Not valid id"})
    serializer = StockSerializer(data)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def StockYearlyAPIView(self, request, pk=None, format=None):
    data = Stock.objects.get(id=pk)
    if data is None:
        return Response({"message":"Not valid id"})
    serializer = StockSerializer(data)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def StockWeeklyAPIView(self, request, pk=None, format=None):
    data = Stock.objects.get(id=pk)
    if data is None:
        return Response({"message":"Not valid id"})
    serializer = StockSerializer(data)
    return Response(serializer.data)