from django.contrib import admin
from .models import Employee, Supplier, Customer
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'position', 'address', 'created_at', 'updated_at')
    search_fields = ('name', 'phone_number', 'email', 'position', 'address')
    list_filter = ('name', 'position')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone_number', 'email', 'address', 'created_at', 'updated_at')
    search_fields = ('name', 'contact_person', 'phone_number', 'email', 'address')
    list_filter = ('name', 'contact_person')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'address', 'created_at', 'updated_at')
    search_fields = ('name', 'phone_number', 'email', 'address')
    list_filter = ('name',)