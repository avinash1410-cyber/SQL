from django.db import models
from stock.models import Stock
from account.models import Customer

# Create your models here.
class Watchlist(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    stock=models.ManyToManyField(Stock,null=True,blank=True)
    cust=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE)