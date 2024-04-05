from django.contrib import admin
from .models import ManureRemoval

class ManureRemovalAdmin(admin.ModelAdmin):
    list_display = ('date_of_removal', 'destination', 'quantity')
    list_filter = ('date_of_removal', 'destination')
    search_fields = ('destination',)
    date_hierarchy = 'date_of_removal'
    list_per_page = 25

admin.site.register(ManureRemoval, ManureRemovalAdmin)