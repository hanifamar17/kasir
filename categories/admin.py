from django.contrib import admin
from .models import Category, Product
# Register your models here.



# Mengubah label di sidebar admin
admin.site.index_title = "Kasir Management"
admin.site.site_header = "SBMS Connect Admin Panel"
admin.site.site_title = "Kasir Admin"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_number', 'name', 'qty', 'unit', 'price', 'total', 'category', 'created_at', 'updated_at')
    search_fields = ('product_number', 'name')
    list_filter = ('unit', 'category', 'created_at')