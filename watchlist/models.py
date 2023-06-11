from django.db import models
from stock.models import Stock
from account.models import Customer

# Create your models here.
class Watchlist(models.Model):
    stock=models.ForeignKey(Stock,null=True,blank=True,on_delete=models.CASCADE)
    user=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.stock.name+""+str(self.id)