# Generated by Django 4.2.4 on 2023-09-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_product_product_id_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=4),
        ),
    ]
