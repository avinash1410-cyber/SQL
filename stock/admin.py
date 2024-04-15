from django.contrib import admin

# Register your models here.
from .models import Stock

class StockAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Stock._meta.fields]  # Specify the fields you want to display in the list view

admin.site.register(Stock,StockAdmin)