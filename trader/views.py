from rest_framework.views import APIView

from account.models import Customer
from design.models import Design
from design.serializers import DesignSerilaizer
from .models import Trader
from .serializers import TraderSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TraderAPIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            data = Trader.objects.get(id=pk)
            serializer = TraderSerializer(data)
        else:
            data = Trader.objects.all()
            serializer = TraderSerializer(data,many=True)
        return Response(serializer.data)


# class TraderOptions(APIView):
#     # permission_classes=[IsAuthenticated]
#     def get(self,request,pk=None):
#         if pk==None:
#             cust=Customer.objects.get(user=request.user)
#             artist=Trader.objects.get(cust=cust)
#         else:
#             artist=Trader.objects.get(id=pk)
#         design=Design.objects.filter(artist=artist)
#         srlzr=DesignSerilaizer(design,many=True)
#         return Response(srlzr.data)





# class AddDataAPIView(APIView):
#     permission_classes=[IsAuthenticated]
#     def post(self,request):
#         design=request.data['design']
#         img=request.data['image']
#         cust=Customer.objects.get(user=request.user)
#         artist=Artist.objects.get(cust=cust)
#         if artist!=None:
#             design=Design.objects.create(design=design,image=img,artist=artist)
#             design.save()
#             return Response({"Message":"Done"})
#         else:
#             return Response({"Message":"Be an artist first"})
#     def get(self,request):
#         return Response({"design":"","image":""})