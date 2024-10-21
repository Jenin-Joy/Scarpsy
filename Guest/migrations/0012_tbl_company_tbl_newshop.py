# Generated by Django 5.0.6 on 2024-08-26 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_tbl_subcategory'),
        ('Guest', '0011_remove_tbl_newshop_place_delete_tbl_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=50)),
                ('Company_Email', models.CharField(max_length=50)),
                ('Company_Contact', models.CharField(max_length=50)),
                ('Company_Address', models.CharField(max_length=50)),
                ('Company_Photo', models.FileField(upload_to='Assets/NewShop/Photo/')),
                ('Company_Proof', models.FileField(upload_to='Assets/NewShop/Proof/')),
                ('Company_status', models.IntegerField(default='0')),
                ('Company_Password', models.CharField(max_length=30)),
                ('Place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_newShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shop_Name', models.CharField(max_length=50)),
                ('Shop_Email', models.CharField(max_length=50)),
                ('Shop_Contact', models.CharField(max_length=50)),
                ('Shop_Address', models.CharField(max_length=50)),
                ('Shop_Photo', models.FileField(upload_to='Assets/NewShop/Photo/')),
                ('Shop_Proof', models.FileField(upload_to='Assets/NewShop/Proof/')),
                ('Shop_status', models.IntegerField(default='0')),
                ('Shop_Password', models.CharField(max_length=30)),
                ('Place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
