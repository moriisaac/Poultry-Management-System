
from django.contrib import admin
from .models import OtherSupply

class OtherSupplyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'expiry_date', 'price', 'supplier_name')
    list_filter = ('category', 'expiry_date')
    search_fields = ('name', 'supplier_name')
    date_hierarchy = 'expiry_date'
    list_per_page = 25

admin.site.register(OtherSupply, OtherSupplyAdmin)
