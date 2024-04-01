# In medicine/admin.py

from django.contrib import admin
from .models import Medicine

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'stage', 'expiry_date', 'price', 'supplier_name', 'medicine_type')
    list_filter = ('medicine_type', 'expiry_date')
    search_fields = ('name', 'stage', 'supplier_name')
    ordering = ('-expiry_date',)
    list_per_page = 25

admin.site.register(Medicine, MedicineAdmin)
