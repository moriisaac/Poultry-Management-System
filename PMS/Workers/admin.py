from django.contrib import admin
from .models import Worker

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_information', 'role', 'hourly_rate', 'date_employed', 'monthly_salary')
    search_fields = ('name', 'contact_information', 'role')
    list_per_page = 25

admin.site.register(Worker, WorkerAdmin)