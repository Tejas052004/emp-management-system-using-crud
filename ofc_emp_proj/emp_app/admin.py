from django.contrib import admin
from .models import Department, Role, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Employee)    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dept', 'salary', 'bonus', 'phone', 'hire_date')