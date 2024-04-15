from django.contrib import admin

from order.models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]  # Specify the fields you want to display in the list view

admin.site.register(Order,OrderAdmin)