from django.contrib import admin

from watchlist.models import Watchlist

# Register your models here.

class WatchlistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Watchlist._meta.fields]  # Specify the fields you want to display in the list view

admin.site.register(Watchlist,WatchlistAdmin)