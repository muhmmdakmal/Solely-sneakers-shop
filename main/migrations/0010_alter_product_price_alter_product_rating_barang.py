# Generated by Django 5.1.1 on 2024-10-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating_barang',
            field=models.IntegerField(default=0),
        ),
    ]
