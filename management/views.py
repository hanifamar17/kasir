from django.shortcuts import render
from .models import Employee, Supplier, Customer

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee.html', {'employees': employees})

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier.html', {'suppliers': suppliers})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})