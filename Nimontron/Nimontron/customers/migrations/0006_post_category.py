# Generated by Django 4.0 on 2022-01-04 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_restaurant_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]