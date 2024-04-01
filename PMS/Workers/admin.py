# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Worker

class WorkerInline(admin.StackedInline):
    model = Worker
    can_delete = False
    verbose_name_plural = 'Worker'

class CustomUserAdmin(UserAdmin):
    inlines = (WorkerInline,)

admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)
