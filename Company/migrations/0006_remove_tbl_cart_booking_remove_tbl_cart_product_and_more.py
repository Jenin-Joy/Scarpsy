# Generated by Django 5.1.2 on 2024-10-17 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0005_tbl_booking_tbl_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_cart',
            name='booking',
        ),
        migrations.RemoveField(
            model_name='tbl_cart',
            name='product',
        ),
        migrations.DeleteModel(
            name='tbl_booking',
        ),
        migrations.DeleteModel(
            name='tbl_cart',
        ),
    ]
