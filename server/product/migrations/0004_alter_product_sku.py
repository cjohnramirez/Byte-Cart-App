# Generated by Django 5.1.5 on 2025-01-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_discount_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='SKU',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
