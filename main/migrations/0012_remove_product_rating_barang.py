# Generated by Django 5.1.1 on 2024-10-04 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating_barang',
        ),
    ]
