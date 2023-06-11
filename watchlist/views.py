import re
from django.shortcuts import redirect
from rest_framework.views import APIView

from account.models import Customer
from stock.models import Stock
from .models import Watchlist
from .serializers import WatchlistSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class WatchlistAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk=None, format=None):
        if pk:
            print(pk)
            cust=Customer.objects.get(user=request.user)
            data = Watchlist.objects.get(id=pk,user=cust)
            if data is None:
                return Response({"Message":"This Item Not exist"})
            serializer = WatchlistSerializer(data)
            return Response(serializer.data)
        else:
            cust=Customer.objects.get(user=request.user)
            if cust!=None:
                data = Watchlist.objects.filter(user=cust)
                serializer = WatchlistSerializer(data,many=True)
                return Response(serializer.data)




class AddDataAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk=None, format=None):
        cust=Customer.objects.get(user=request.user)
        if cust!=None:
            product=Stock.objects.get(id=pk)
            cart=Watchlist.objects.create(product=product,user=cust)
            cart.save()
            return redirect("MyWatchlist")
        else:
            return Response({"Message":"First Made an Acoount"})