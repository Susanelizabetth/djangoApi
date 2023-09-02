
from django.contrib import admin

from .models import User, View, Role

# Register your models here.


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'organization_role', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'organization_role')
    list_editable = ('is_active', 'is_staff', 'organization_role')
