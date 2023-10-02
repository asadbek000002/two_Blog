from django.contrib import admin
from .models import Actions

@admin.register(Actions)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['user', 'verb', 'target', 'create']
    list_filter = ['create']
    search_fields = ['verb']
