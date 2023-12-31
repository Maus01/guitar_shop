# Generated by Django 4.2.4 on 2023-09-04 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_product_product_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='image_banner',
        ),
        migrations.AddField(
            model_name='category',
            name='image_index',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
