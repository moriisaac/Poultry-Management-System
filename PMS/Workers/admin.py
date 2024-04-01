from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import  CustomUser



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Define custom fields to display in the admin interface
    list_display = ['username', 'email', 'role', 'is_staff','date_employed', 'monthly_salary']

admin.site.register(CustomUser, CustomUserAdmin)
