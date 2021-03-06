# Generated by Django 4.0.4 on 2022-05-07 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0004_rename_customer_post_customerpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerpost',
            name='contact_no',
        ),
        migrations.AlterField(
            model_name='customerpost',
            name='area',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customerpost',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customerpost',
            name='description',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customerpost',
            name='quantity',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(choices=[('payment2', 'payment2'), ('payment3', 'payment3'), ('payment1', 'payment1')], default='payment3', max_length=20),
        ),
    ]
