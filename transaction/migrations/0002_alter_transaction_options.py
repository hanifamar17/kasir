# Generated by Django 5.1.1 on 2025-01-12 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'Transaction', 'verbose_name_plural': 'Transactions'},
        ),
    ]