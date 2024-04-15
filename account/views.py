from rest_framework import generics
# Create your views here.
from rest_framework.views import APIView
from rest_framework import status

from trader.models import Trader
from trader.serializers import TraderSerializer
from .models import Customer

from stock.models import Stock
from stock.serializers import StockSerializer
from order.models import Order
from order.serializers import OrderSerializer


from watchlist.models import Watchlist
from watchlist.serializers import WatchlistSerializer


from django.shortcuts import get_object_or_404
from .serializers import ChangePasswordSerializer, CustomerSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated







from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status







@api_view(('GET','POST'))
def register_page(request):
    if request.method == "POST":
        userName = request.data['username']
        userPass = request.data['password']
        userMail = request.data['email']
        phone=request.data['phone']
        address=request.data['add']
        userBalance = request.data['balance']
        user = User.objects.create_user(userName, userMail, userPass)
        cust=Customer.objects.create(
            user=user,
            add=address,
            phone=phone,
            balance=userBalance
        )
        return Response({"message":"Registration done"})
    return Response({"username":"","password":"","email":"","phone":"","add":"","balance":"0"})


@api_view(('GET','POST'))
def login_page(request):
    print("IN LOGIN")
    if request.method == "POST":
        username = request.data['username']
        password=request.data['password']
        print(request.user)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print(request.user)
            return Response({"message":"Login done"})
        else:
            return Response({"message":"Invalid Credentials"})
    return Response({"username":"","password":""})



@api_view(('GET',))
def logout_page(request):
    logout(request)
    return Response({'message':"Logged out"})




class update_trader(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        cust = get_object_or_404(Customer, user=request.user)
        trader_exists = Trader.objects.filter(cust=cust).exists()        
        if not trader_exists:
            Trader.objects.create(cust=cust, Trader=True)
            return Response({'message': 'Trader Created Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You are already a Trader'}, status=status.HTTP_200_OK)


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
        data = f'Congratulations, your API just responded to the POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)



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


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def buyStock(request,pk=None):
    if request.method == 'POST':
        stock_id=request.data["stock_id"]
        amount=int(request.data["amount"])
        quantity=0

        cust=Customer.objects.get(user=request.user)
        stock=Stock.objects.get(id=stock_id)
        if int(amount)<stock.price:
            message=f'Your amount is so much low please send at least Rs.{stock.price}.'
            return Response({'message': message}, status=status.HTTP_200_OK)
        quantity=amount//int(stock.price)
        order=Order.objects.create(
            quantity=quantity,
            amount=amount,
            cust=cust,
            stock=stock,
        )
        order.save()
        data = f'Congratulation your API just responded to POST request with text'
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        return Response({'amount':'','stock_id':''}, status=status.HTTP_200_OK)
    return Response({"message":"Request Not allowed"}, status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def sellStock(request,pk=None,id=None):
    if request.method == 'GET':
        return Response({'quantity':'','stock_id':'','price':''}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        quantity=int(request.data["quantity"])
        price=request.data["price"]
        stock_id=request.data["stock_id"]
        cust=Customer.objects.get(user=request.user)
        stock=Stock.objects.get(id=stock_id)
        try:
            order=Order.objects.get(cust=cust,stock_id=stock)
        except Order.DoesNotExist:
            order = None
            return Response({"Message":"Order Not Exist"},status=status.HTTP_200_OK)
        
        quantity_have=int(order.quantity)
        if quantity_have<=0:
            return Response({'message':f"You can't sell as u have {quantity_have} no of stocks please buy first"}, status=status.HTTP_200_OK)
        if quantity_have-quantity<0:
            return Response({'message':f"You can't sell as u have {quantity_have} no of stocks please buy first and u are trying to sell {quantity} no of stocks please decrease the quantity u want to sell"}, status=status.HTTP_200_OK)
        new_quantity=int(quantity_have-quantity)
        if new_quantity==0:
            order.delete()
        else:
            order.quantity=new_quantity
            order.save()
        company=stock.name
        text=f" u have sell {quantity} no of stock of {company} stocks"
        data = f'{text}'
        return Response({'message': data}, status=status.HTTP_200_OK)
    return Response({"message":"Request Not allowed"}, status.HTTP_400_BAD_REQUEST)


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




@api_view(['GET',])
@permission_classes([IsAuthenticated])
def HiresList(request, pk=None):
    if request.method == 'GET':
        if pk is None:  # If pk is not provided, default to the authenticated user's ID
            pk = request.user.id
        data = Trader.objects.filter(client_id=pk)        
        serializer = TraderSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def addToWatchlist(request,id=None):
    if request.method == 'GET':
        return Response({'stock_id':'','watchlist_id':'','name':''}, status=status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'POST':
        try:
            # Get the Stock and User objects
            stock_id=int(request.data['stock_id'])
            watchlist_id=request.data['watchlist_id']
            stock = Stock.objects.get(id=stock_id)
            cust = Customer.objects.get(user=request.user)
            if not watchlist_id:
                name=request.data['name']
                watchlist=Watchlist.objects.create(name=name,cust=cust)
            else:
                watchlist = Watchlist.objects.get(id=watchlist_id,cust=cust)
            watchlist.stock.add(stock)
            watchlist.save()
            # Return success response
            return Response({'response': 'Watchlist item added successfully'}, status=status.HTTP_201_CREATED)
        except Stock.DoesNotExist:
            return Response({'error': 'Stock does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def myWatchlist(request,id=None):
    if request.method == 'GET':
        cust = Customer.objects.get(user=request.user)
        try:
            # Check if a watchlist already exists for the customer
            watchlist = Watchlist.objects.get(cust=cust)
        except Watchlist.DoesNotExist:
           return Response({'error': 'No any Watchlist Found'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = WatchlistSerializer(data=watchlist,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Request Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Status(request):
    if request.method == 'GET':
        data = f"{request.user}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)