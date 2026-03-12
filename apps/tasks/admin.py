from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'board', 'list', 'priority', 'created_by', 'due_date', 'is_archived']
    list_filter = ['priority', 'is_archived', 'due_date', 'created_at']
    search_fields = ['title', 'description']
    filter_horizontal = ['assigned_to']
    date_hierarchy = 'created_at'

