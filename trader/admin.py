from re import A
from django.contrib import admin

# Register your models here.
from .models import Trader
admin.site.register(Trader)