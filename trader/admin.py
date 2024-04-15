from re import A
from django.contrib import admin

# Register your models here.
from .models import Trader

class TraderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Trader._meta.fields]  # Specify the fields you want to display in the list view

admin.site.register(Trader,TraderAdmin)