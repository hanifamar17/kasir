from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import transaction
from .models import Transaction, TransactionItem
from categories.models import Product
import json

@login_required
def cashier_view(request):
    products = Product.objects.all()
    return render(request, 'cashier.html', {'products': products})

@login_required
def get_product(request):
    code = request.GET.get('code', '').strip()
    if not code:
        return JsonResponse({'error': 'Product code is required'}, status=400)
    
    try:
        product = Product.objects.get(product_number=code)
        if product.qty <= 0:
            return JsonResponse({'error': 'Product is out of stock'}, status=400)
        
        return JsonResponse({
            'product_number': product.product_number,
            'name' : product.name,
            'price' : str(product.price),
            'stock' : product.qty
        })
    
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def save_transaction(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid method'}, status=405)

    data = json.loads(request.body)
    print(data)  # Untuk melihat data yang diterima oleh server
    items = data.get('items', [])
    
    if not items:
        return JsonResponse({'error': 'No items in transaction'}, status=400)

    try:
        with transaction.atomic():
            # Create transaction
            new_transaction = Transaction.objects.create(
                employee=request.user.employee,
                customer_id=data['customer_id'],
                total_amount=data['total_amount'],
                payment_method=data['payment_method'],
                paid_amount=data['paid_amount'],
                change_amount=data['change_amount'],
                status='COMPLETED'
            )

            # Create transaction items
            for item in items:
                product = Product.objects.get(product_number=item['product_number'])
                TransactionItem.objects.create(
                    transaction=new_transaction,
                    product=product,
                    qty=item['quantity'],
                    unit_price=item['price'],
                    subtotal=item['subtotal']
                )

                # Update stock
                product.qty -= item['quantity']
                product.save()

        return JsonResponse({
            'success': True,
            'transaction_id': new_transaction.id
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


