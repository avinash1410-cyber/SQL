# Generated by Django 4.0.1 on 2024-04-13 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_price_order_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='cust',
        ),
    ]
