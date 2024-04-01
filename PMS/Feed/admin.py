# In feed/admin.py

from django.contrib import admin
from .models import Feed

class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'expiry_date', 'administration_method', 'price', 'supplier_name', 'feeding_time', 'quantity_bought', 'quantity_used', 'total_quantity_remaining', 'is_quantity_below_threshold')
    list_filter = ('type', 'expiry_date', 'administration_method', 'supplier_name', 'feeding_time')
    search_fields = ('name', 'type', 'supplier_name')
    ordering = ('-feeding_time',)
    list_per_page = 25

    def is_quantity_below_threshold(self, obj):
        return obj.is_quantity_below_threshold

    is_quantity_below_threshold.boolean = True
    is_quantity_below_threshold.short_description = 'Below Threshold'

admin.site.register(Feed, FeedAdmin)
