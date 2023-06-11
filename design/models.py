from django.db import models
from trader.models import Trader
from cloudinary.models import CloudinaryField

# Create your models here.
class Design(models.Model):
    design=models.CharField(max_length=100,null=True,blank=True)
    artist=models.ForeignKey(Trader,on_delete=models.CASCADE,null=True,blank=True)
    image=CloudinaryField('image')