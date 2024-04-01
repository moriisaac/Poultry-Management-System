

# Register your models here.
from django.contrib import admin
from .models import Feed

class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'expiry_date', 'administration_method', 'price', 'supplier_name','feeding_time','quantity_used')
    list_filter = ('type', 'expiry_date')
    search_fields = ('name', 'type', 'supplier_name')
    ordering = ('expiry_date',)
    list_per_page = 25

admin.site.register(Feed, FeedAdmin)