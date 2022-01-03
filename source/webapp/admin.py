from django.contrib import admin

# Register your models here
from webapp.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'detailed_description', 'status', 'create_until']
    list_filter = ['status']
    search_fields = ['description', 'status']
    fields = ['description', 'detailed_description', 'status', 'create_until']
    readonly_fields = ['create_until']

admin.site.register(Task, TaskAdmin)