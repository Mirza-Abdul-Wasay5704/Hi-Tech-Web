from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'location', 'completion_date']
    list_filter = ['completion_date']
    search_fields = ['title', 'client', 'location']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ProjectImageInline]
