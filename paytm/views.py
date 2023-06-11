from traceback import print_tb
from django.http import HttpResponse
from .import PaytmChecksum
from stock.models import Stock
from order.models import Order
from django.views.decorators.csrf import csrf_exempt
from account.models import Customer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
MERCHANTID='aRQfpN33171736399046'
YOUR_MERCHANT_KEY='AbVHoFGJtyRtMJA2'
from rest_framework.response import Response
from django.shortcuts import render


@csrf_exempt
@api_view(['GET', 'POST'])
def start_payment(request):
    userid = request.data['userid']
    productid = request.data['productid']
    address = request.data['address']
    amount = request.data['amount']

    product=Stock.objects.get(id=productid)
    user=User.objects.get(id=userid)
    cust=Customer.objects.get(user=user)
    order=Order.objects.create(product=product,user=cust,address=address)
    order.save()
    print(order.id,userid,productid,address,amount)
    body ={
            'MID': MERCHANTID,
            'ORDER_ID': str(order.id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': cust.id,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            # this is the url of handlepayment function, paytm will send a POST request to the fuction associated with this CALLBACK_URL
        }

    # Generate checksum by parameters we have
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    paytmChecksum = PaytmChecksum.generateSignature(body, YOUR_MERCHANT_KEY)
    print("generateSignature Returns:" + str(paytmChecksum))
    # return HttpResponse("Start is ended")
    body['CHECKSUMHASH']=paytmChecksum
    print(body)
    return Response({'body':body})    

@csrf_exempt
@api_view(['POST'])
def handlepayment(request):
    print("IN the Handle")
    print(request.data)
    MERCHANT_KEY = YOUR_MERCHANT_KEY
    data_dict = {}
    for key in request.data:
        data_dict[key] = request.data[key]
    paytmChecksum = data_dict['CHECKSUMHASH']
    verify = PaytmChecksum.verifySignature(data_dict, MERCHANT_KEY, paytmChecksum)
    if verify:
        print("Checksum Matched")
        # return render(request,"response.html",{"paytm":data_dict})
        order=Order.objects.get(id=data_dict['ORDERID'])
        order.isPaid=True
        order.save()
        return render(request, 'paytm/paymantstatus.html', {'response': data_dict})
    else:
        print("Checksum Mismatched")
        return render(request, 'paytm/paymantstatus.html', {'response': data_dict})