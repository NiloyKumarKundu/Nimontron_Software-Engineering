# Generated by Django 4.0.1 on 2022-01-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0019_cart_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
