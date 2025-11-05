from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'due_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'due_date'

    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Detalles', {
            'fields': ('due_date', 'is_completed'),
            'classes': ('collapse',),
        }),
    )
admin.site.register(Task, TaskAdmin)