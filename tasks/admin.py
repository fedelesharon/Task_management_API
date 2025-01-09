from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'due_date', 'completed', 'priority')
    # Fields to filter by in the admin list view
    list_filter = ('completed', 'priority')
    # Fields to search by in the admin list view
    search_fields = ('title', 'description')

# Register the Task model with the customized TaskAdmin
admin.site.register(Task, TaskAdmin)

