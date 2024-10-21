# Generated by Django 5.0.6 on 2024-08-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_delete_tbl_newshop'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_newShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NewShop_Name', models.CharField(max_length=50)),
                ('NewShop_Email', models.CharField(max_length=50)),
                ('NewShop_Contact', models.CharField(max_length=50)),
                ('NewShop_Address', models.CharField(max_length=50)),
                ('NewShop_Place', models.CharField(max_length=50)),
                ('NewShop_Photo', models.FileField(upload_to='Assets/NewShop/Photo/')),
                ('NewShop_Proof', models.FileField(upload_to='Assets/NewShop/Proof/')),
            ],
        ),
    ]
