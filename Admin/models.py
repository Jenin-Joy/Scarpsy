from django.db import models

# Create your models here.

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
class tbl_Registration(models.Model):
    Registration_name=models.CharField(max_length=50)
    Registration_email=models.CharField(max_length=50)
    Registration_password=models.CharField(max_length=50)

class tbl_Place(models.Model):
    Place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)