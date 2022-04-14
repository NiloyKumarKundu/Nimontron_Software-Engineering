# Generated by Django 4.0.3 on 2022-03-26 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0022_alter_foundation_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_Man',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('ratting', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
