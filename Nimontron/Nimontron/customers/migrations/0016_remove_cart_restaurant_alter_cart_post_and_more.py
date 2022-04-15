# Generated by Django 4.0.1 on 2022-01-23 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0015_delete_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='restaurant',
        ),
        migrations.AlterField(
            model_name='cart',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.post'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('Cart', 'Cart'), ('Active', 'Active'), ('Delivered', 'Delivered')], default='Cart', max_length=20),
        ),
    ]
