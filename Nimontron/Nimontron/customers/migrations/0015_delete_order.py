# Generated by Django 4.0.1 on 2022-01-23 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0014_remove_cart_customer_cart_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
