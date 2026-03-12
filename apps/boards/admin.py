from django.contrib import admin
from .models import Board, BoardList


class BoardListInline(admin.TabularInline):
    model = BoardList
    extra = 1
    ordering = ['position']


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'workspace', 'created_by', 'created_at', 'is_archived']
    list_filter = ['is_archived', 'created_at', 'workspace']
    search_fields = ['name', 'description']
    inlines = [BoardListInline]


@admin.register(BoardList)
class BoardListAdmin(admin.ModelAdmin):
    list_display = ['name', 'board', 'position', 'is_archived']
    list_filter = ['is_archived', 'board']
    search_fields = ['name']

