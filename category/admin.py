from django.contrib import admin

# Register your models here.
from .models import Categories
class CategoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Categories._meta.fields]  # Specify the fields you want to display in the list view

admin.site.register(Categories,CategoriesAdmin)