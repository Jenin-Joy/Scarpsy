# Generated by Django 5.1.2 on 2024-10-17 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0006_remove_tbl_cart_booking_remove_tbl_cart_product_and_more'),
        ('Guest', '0012_tbl_company_tbl_newshop'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_amount', models.CharField(max_length=30)),
                ('booking_status', models.IntegerField(default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_company')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_qty', models.IntegerField(default=1)),
                ('cart_status', models.IntegerField(default=0)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.tbl_booking')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.tbl_product')),
            ],
        ),
    ]
