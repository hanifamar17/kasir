from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #phone_number = PhoneNumberField(blank=True)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^08[0-9]{8,13}$',
                message='Format nomor telepon harus dimulai dengan 08 dan diikuti 8-13 digit angka'
            )
        ]
    )
    email = models.EmailField(max_length=100)
    position = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False  # Jangan biarkan Django mengelola tabel ini
        db_table = 'employees'  # Nama tabel di database
        verbose_name = "Employee"  # Nama tunggal
        verbose_name_plural = "Employees"  # Nama jamak

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Perusahaan")
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^08[0-9]{8,13}$',
                message='Format nomor telepon harus dimulai dengan 08 dan diikuti 8-13 digit angka'
            )
        ]
    )
    email = models.EmailField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False  # Jangan biarkan Django mengelola tabel ini
        db_table = 'suppliers'  # Nama tabel di database
        verbose_name = "Supplier"  # Nama tunggal
        verbose_name_plural = "Suppliers"  # Nama jamak

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^08[0-9]{8,13}$',
                message='Format nomor telepon harus dimulai dengan 08 dan diikuti 8-13 digit angka'
            )
        ]
    )
    email = models.EmailField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False  # Jangan biarkan Django mengelola tabel ini
        db_table = 'customers'  # Nama tabel di database
        verbose_name = "Customer"  # Nama tunggal
        verbose_name_plural = "Customers"  # Nama jamak