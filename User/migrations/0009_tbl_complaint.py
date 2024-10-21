# Generated by Django 5.0.6 on 2024-09-17 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0012_tbl_company_tbl_newshop'),
        ('User', '0008_delete_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complaint_Title', models.CharField(max_length=50)),
                ('Complaint_Content', models.CharField(max_length=100)),
                ('Complaint_Date', models.DateField(auto_now_add=True)),
                ('Complaint_Replay', models.CharField(max_length=100)),
                ('Complaint_Status', models.IntegerField(default=0)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_company')),
                ('Shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_newshop')),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_user')),
            ],
        ),
    ]
