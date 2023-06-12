from django.db import models
from stock.models import Stock
from account.models import Customer

# Create your models here.
class Order(models.Model):
    stock=models.ForeignKey(Stock,null=True,blank=True,on_delete=models.CASCADE)
    user=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE)
    price=models.CharField(max_length=100,null=True,blank=True)
    quantity =models.CharField(max_length=100,null=True,blank=True)
    orderDate=models.DateTimeField(auto_now=True)
    buy=models.BooleanField(default=True)

    def __str__(self):
        return self.product.name