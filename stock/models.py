from django.db import models
from trader.models import Trader
from account.models import Customer
from category.models import Categories
from cloudinary.models import CloudinaryField

from design.models import Design



class Stock(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    customer=models.ManyToManyField(Customer, null=True,blank=True)
    cat=models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True,blank=True)
    image=CloudinaryField('image',null=True,blank=True)
    market_cap=models.CharField(max_length=10,null=True,blank=True)

    @property
    def get_all_products(self):
        return Stock.objects.all()
    @property
    def disc_price(self):
        return self.price*self.category.disc

    def __str__(self):
        return self.name