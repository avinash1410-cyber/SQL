from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone=models.CharField(max_length=13,blank=True,null=True)
    add=models.CharField(max_length=200,null=True,blank=True)
    balance=models.CharField(max_length=13,blank=True,null=True,default='0')

    def __str__(self):
        return str(self.user)
    @property
    def name(self):
        return self.__str__()