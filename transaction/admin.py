from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from .models import Transaction
# Register your models here.


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'transaction_date']    