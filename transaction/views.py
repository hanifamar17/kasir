from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import transaction
from .models import Transaction, TransactionItem
from categories.models import Product
from management.models import Customer, Employee
import json
import logging
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

@login_required
def cashier_view(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    employees = Employee.objects.all()
    return render(request, 'cashier.html', {'products': products, 'customers': customers, 'employees': employees})

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

    try:
        # Log request body
        print("Raw request body:", request.body.decode('utf-8'))

        data = json.loads(request.body)
        print("Parsed data:", data)
        items = data.get('items', [])
        print("Items:", items)
    
        # Validasi customer
        try:
            customer = Customer.objects.get(id=data['customer_id'])
            print("Customer found:", customer)
        except Customer.DoesNotExist:
            return JsonResponse({'error': f'Customer with id {data["customer_id"]} not found'}, status=400)
        
        # Validasi employee
        try:
            employee = Employee.objects.get(id=data['employee_id'])
        except Employee.DoesNotExist:
            return JsonResponse({'error': f'Employee with id {data["employee_id"]} not found'}, status=400)
        
        # Validasi items
        for item in items:
            required_item_fields = ['product_number', 'quantity', 'price', 'subtotal']
            for field in required_item_fields:
                if field not in item:
                    return JsonResponse({'error': f'Missing required field in item: {field}'}, status=400)

        try:
            with transaction.atomic():
                print("Creating transaction...")
                new_transaction = Transaction.objects.create(
                    employee=employee,
                    customer=customer,
                    total_amount=data['total_amount'],
                    payment_method=data['payment_method'],
                    paid_amount=data['paid_amount'],
                    change_amount=data['change_amount'],
                    status='COMPLETED',
                    transaction_date=timezone.now()
                )
                print("Transaction created:", new_transaction)
                
                for item in items:
                    try:
                        product = Product.objects.get(product_number=item['product_number'])
                        print(f"Processing product: {product}")
                        
                        TransactionItem.objects.create(
                            transaction=new_transaction,
                            product=product,
                            qty=item['quantity'],
                            unit_price=item['price'],
                            subtotal=item['subtotal']
                        )
                        
                        product.qty -= item['quantity']
                        product.save()
                        print(f"Product {product} updated")
                        
                    except Product.DoesNotExist:
                        raise Exception(f'Product with number {item["product_number"]} not found')
                    
                print("All items processed successfully")
                
            return JsonResponse({
                'success': True,
                'transaction_id': new_transaction.id
            })
            
        except Exception as e:
            print("Error dalam transaksi:", str(e))
            raise
            
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", str(e))
        return JsonResponse({'error': f'Invalid JSON format: {str(e)}'}, status=400)
    except Exception as e:
        print("General Error:", str(e))
        print("Error type:", type(e))
        import traceback
        print("Traceback:", traceback.format_exc())
        return JsonResponse({'error': str(e)}, status=400)


