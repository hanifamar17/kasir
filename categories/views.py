from django.shortcuts import render
from .models import Category, Product
# Create your views here.


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def product_list(request):
    products = Product.objects.select_related('category').all()  # Menggunakan select_related untuk efisiensi
    return render(request, 'product.html', {'products': products})