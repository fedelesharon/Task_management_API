from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'priority', 'status')  # Use 'status' instead of 'completed'
    list_filter = ('status', 'priority')  # Use 'status' instead of 'completed'
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)

