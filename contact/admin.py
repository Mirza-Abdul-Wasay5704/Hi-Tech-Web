from django.contrib import admin
from .models import Contact, Quote

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'phone', 'message']
    readonly_fields = ['created_at']

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'service_type', 'created_at', 'is_processed']
    list_filter = ['is_processed', 'created_at', 'service_type']
    search_fields = ['name', 'email', 'phone', 'service_type', 'details']
    readonly_fields = ['created_at']
