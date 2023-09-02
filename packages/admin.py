from django.contrib import admin

from .models import Package

# Register your models here.


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'description', 'value')
    search_fields = ('id', 'order')
    list_editable = ('description', 'value')
