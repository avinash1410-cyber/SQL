from rest_framework.views import APIView
from .models import Stock
from .serializers import StockSerializer
from rest_framework.response import Response
from django.db.models import Q
from cloudinary.forms import cl_init_js_callbacks      
from rest_framework.decorators import api_view, permission_classes
import requests




class StockSearchAPIView(APIView):
    def get(self,request,query=None):
        print("PRINTING THE SLUG",query)
        stocks=Stock.objects.filter(
                              Q(name__icontains=query))
        data=StockSerializer(stocks,many=True)
        return Response(data.data)



class Home(APIView):
    def get(self, request):
        def get_stock_price(symbol):
            api_key = "Y5CIFL2TLHX4S7C6"  # Replace with your Alpha Vantage API key
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"

            try:
                response = requests.get(url)
                data = response.json()

                if "Error Message" in data:
                    return None

                stock_info = data["Global Quote"]
                price = stock_info["05. price"]
                volume = int(stock_info["06. volume"])
                return {"price": price, "volume": volume}

            except requests.exceptions.RequestException:
                return None

        symbols = ["AAPL", "TSLA","MSFT","JPM","V"]
        stock_prices = {}
        for symbol in symbols:
            price = get_stock_price(symbol)
            if price:
                stock_prices[symbol] = price

        return Response(stock_prices)
















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