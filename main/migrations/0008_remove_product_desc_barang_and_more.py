# Generated by Django 5.1.1 on 2024-09-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='desc_barang',
        ),
        migrations.RemoveField(
            model_name='product',
            name='nama_barang',
        ),
        migrations.AlterField(
            model_name='product',
            name='rating_barang',
            field=models.IntegerField(),
        ),
    ]