# Generated by Django 4.2.4 on 2023-09-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbase',
            old_name='is_admin',
            new_name='is_staff',
        ),
        migrations.AlterField(
            model_name='userbase',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
