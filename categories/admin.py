from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_number', 'name', 'qty', 'unit', 'price', 'total', 'category', 'created_at', 'updated_at')
    search_fields = ('product_number', 'name')
    list_filter = ('unit', 'category', 'created_at')