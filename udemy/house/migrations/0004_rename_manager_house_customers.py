# Generated by Django 5.0 on 2024-04-09 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_rename_customer_house_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='manager',
            new_name='customers',
        ),
    ]
