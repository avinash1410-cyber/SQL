from django.contrib import admin

from design.models import Design

# Register your models here.
class DesignAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Design._meta.fields]  # Specify the fields you want to display in the list view

admin.site.register(Design,DesignAdmin)