from django.contrib import admin
from .models import TodoList

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ("task","start_date","end_date","completed")
admin.site.register(TodoList,TodoAdmin)