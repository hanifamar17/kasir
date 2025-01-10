from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False  # Jangan biarkan Django mengelola tabel ini
        db_table = 'categories'  # Nama tabel di database

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    unit = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Total bisa kosong
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Foreign key
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        managed = False  # Karena tabel sudah ada di database

    # Signal untuk menghitung total sebelum menyimpan
@receiver(pre_save, sender=Product)
def calculate_total(sender, instance, **kwargs):
    if instance.price and instance.qty:  # Pastikan price dan qty diisi
        instance.total = instance.price * instance.qty
