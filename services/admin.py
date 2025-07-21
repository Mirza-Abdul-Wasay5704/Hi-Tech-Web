from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
