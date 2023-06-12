from rest_framework import generics
# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from trader.models import Trader
from .models import Customer
from stock.models import Stock
from order.models import Order
from watchlist.models import Watchlist
from .serializers import ChangePasswordSerializer, CustomerSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(('GET','POST'))
def register_page(request):
    if request.method == "POST":
        userName = request.data['username']
        userPass = request.data['password']
        userMail = request.data['email']
        phone=request.data['phone']
        address=request.data['add']
        user = User.objects.create_user(userName, userMail, userPass)
        cust=Customer.objects.create(
            user=user,
            add=address,
            phone=phone,
        )
        return Response({"message":"Registration done"})
    return Response({"username":"","password":"","email":"","phone":"","add":""})


@api_view(('GET','POST'))
def login_page(request):
    if request.method == "POST":
        username = request.data['username']
        password=request.data['password']
        print(request.user)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return Response({"message":"Login done"})
        else:
            return Response({"message":"Invalid Credentials"})
    return Response({"username":"","password":""})



@api_view(('GET',))
def logout_page(request):
    logout(request)
    return Response({'message':"Logged out"})




class update_trader(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        print(request.user)
        cust=Customer.objects.get(user=request.user)
        if cust is None:
            return Response({"Message":"You are not an valid user"})
        Trader.objects.create(cust=cust,Trader=True)
        return Response({'message': 'Trader Created Successfully'})



class CustomerAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk=None, format=None):
        data = Customer.objects.get(user=request.user)
        serializer = CustomerSerializer(data)
        return Response(serializer.data)




class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer()
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def addBalance(request,pk=None):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        deposit = pk
        cust=Customer.objects.get(user=request.user)
        previous_balance=Customer.balance
        new_balance=pk+previous_balance
        cust.balance=new_balance
        cust.save()
        # data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': cust.balance}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def withdrawBalance(request,pk=None):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        credit = pk
        cust=Customer.objects.get(user=request.user)
        previous_balance=Customer.balance
        new_balance=previous_balance-pk
        cust.balance=new_balance
        cust.save()
        # data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': cust.balance}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def buyStock(request,pk=None,id=None):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        quantity=id
        price=pk
        user=Customer.objects.get(user=request.user)
        stock=Stock.objects.get(id=pk)
        order=Order.create(
            quantity=quantity,
            price=price,
            user=user,
            stock=stock,
        )
        order.save()
        # data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def sellStock(request,pk=None,id=None):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        quantity=id
        price=pk
        user=Customer.objects.get(user=request.user)
        stock=Stock.objects.get(id=pk)
        order=Order.create(
            quantity=quantity,
            price=price,
            user=user,
            stock=stock,
            buy=False,
        )
        order.save()
        # data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def buyOption(request):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def sellOption(request):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def hireTrader(request,pk):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        id=pk
        trader=Trader.objects.get(id=pk)
        user=Customer.objects.get(user=request.user)
        trader.clients=trader.clients+user
        trader.save()
        # data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def searchTrader(request,pk=None):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        id=pk
        trader=Trader.objects.get(id=pk)
        # data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def seeRecordOfTrader(request,pk=None):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        id=pk
        trader=Trader.objects.get(id=pk)
        # data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def addToWatchlist(request,pk=None,id=None):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        stock=Stock.objects.get(id=pk)
        user=Customer.objects.get(user=request.user)
        watchlist=Watchlist(
            stock=stock,
            user=user,
        )
        watchlist.save()
        # data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def status(request):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)