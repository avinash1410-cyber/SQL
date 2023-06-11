from django.db import models
from stock.models import Stock
from account.models import Customer

# Create your models here.
class Order(models.Model):
    product=models.ForeignKey(Stock,null=True,blank=True,on_delete=models.CASCADE)
    user=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE)
    address=models.CharField(max_length=100,null=True,blank=True)
    isPaid = models.BooleanField(default=False)
    orderDate=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name