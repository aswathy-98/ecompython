# Generated by Django 3.2.18 on 2023-04-18 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]
