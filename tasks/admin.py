from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task  # Import your Task model

# Register your Task model in the Django Admin interface
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Display fields in the task list view
    list_display = ('id', 'title', 'description', 'completed', 'created_at', 'updated_at')
    
    # Add search functionality for the title and description fields
    search_fields = ('title', 'description')
    
    # Add filters for the task status
    list_filter = ('completed', 'created_at')

    # Optionally, add fieldsets to organize form layout when adding/editing tasks
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'completed')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

