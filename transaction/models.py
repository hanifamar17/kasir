from django.db import models
from django.utils import timezone

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELED', 'Canceled'),
    ]
    PAYMENT_CHOICES = [
        ('CASH', 'Cash'),
        ('CARD', 'Card'),
        ('TRANSFER', 'Transfer'),
    ]
    employee  = models.ForeignKey('management.Employee', on_delete=models.CASCADE)
    customer = models.ForeignKey('management.Customer', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES) 
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    change_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    transaction_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction #{self.id} - {self.transaction_date}"
    
    class Meta:
        managed = False# Jangan biarkan Django mengelola tabel ini
        db_table = 'transactions'  # Nama tabel di database
        verbose_name = "Transaction"  # Nama tunggal
        verbose_name_plural = "Transactions"  # Nama jamak

class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('categories.Product', on_delete=models.PROTECT)
    qty = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.subtotal = self.qty * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} x #{self.qty}"
    
    class Meta:
        managed = False  # Jangan biarkan Django mengelola tabel ini
        db_table = 'transaction_items'  # Nama tabel di database
        verbose_name = "Transaction Item"  # Nama tunggal
        verbose_name_plural = "Transaction Items"  # Nama jamak
