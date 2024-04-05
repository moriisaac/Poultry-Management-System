from django.contrib import admin
from .models import Poultry

class PoultryAdmin(admin.ModelAdmin):
    list_display = ('poultry_house', 'poultry_type', 'total_quantity', 'kienyeji_grown_quantity', 'broilers_grown_quantity', 'layers_grown_quantity', 'chicks_type', 'kienyeji_chicks_quantity', 'broilers_chicks_quantity', 'layers_chicks_quantity')
    list_filter = ('poultry_house', 'poultry_type', 'chicks_type')
    search_fields = ('poultry_house__pen_number',)
    ordering = ('-id',)
    list_per_page = 25

admin.site.register(Poultry, PoultryAdmin)
