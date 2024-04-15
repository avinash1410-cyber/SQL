from django.contrib import admin

# Register your models here.
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]  # Specify the fields you want to display in the list view
admin.site.register(Customer,CustomerAdmin)