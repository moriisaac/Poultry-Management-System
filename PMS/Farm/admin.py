from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('id','name','owner','location','contact_info')
    list_display_links =  ('name','location')
    list_filter = ('location','contact_info')
    search_fields = ('id', 'name', 'contact_info')
    list_per_page = 10

@admin.register(PoultryHouse)
class PoultryHouseAdmin(admin.ModelAdmin):
    list_display = ('id','farm','pen_no','mortality_rate','production_rate','capacity','temperature','humidity')
    list_display_links = ('farm','pen_no','mortality_rate','production_rate','capacity')
    list_filter = ('capacity','farm')
    search_fields = ('id','capacity','farm','production_rate')
    list_per_page = 10