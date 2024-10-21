from django.db import models
from Admin.models import *
from Guest.models import *

#Create your models here.

class tbl_user(models.Model):
    User_Name=models.CharField(max_length=50)
    User_Address=models.CharField(max_length=50)
    User_Contact=models.CharField(max_length=50)
    User_Email=models.CharField(max_length=50)
    Place=models.ForeignKey(tbl_Place,on_delete=models.CASCADE)
    User_Gender=models.CharField(max_length=50)
    User_Dob=models.CharField(max_length=50)
    User_Password=models.CharField(max_length=50)
    User_Photo = models.FileField(upload_to="Assets/User/")

class tbl_newShop(models.Model):
    Shop_Name=models.CharField(max_length=50)
    Shop_Email=models.CharField(max_length=50)
    Shop_Contact=models.CharField(max_length=50)
    Shop_Address=models.CharField(max_length=50)
    Place=models.ForeignKey(tbl_Place, on_delete=models.CASCADE)
    Shop_Photo=models.FileField(upload_to="Assets/NewShop/Photo/")
    Shop_Proof = models.FileField(upload_to="Assets/NewShop/Proof/")
    Shop_status=models.IntegerField(default="0")
    Shop_Password = models.CharField(max_length=30)

class tbl_company(models.Model):
    Company_Name=models.CharField(max_length=50)
    Company_Email=models.CharField(max_length=50)
    Company_Contact=models.CharField(max_length=50)
    Company_Address=models.CharField(max_length=50)
    Place=models.ForeignKey(tbl_Place, on_delete=models.CASCADE)
    Company_Photo=models.FileField(upload_to="Assets/NewShop/Photo/")
    Company_Proof = models.FileField(upload_to="Assets/NewShop/Proof/")
    Company_status=models.IntegerField(default="0")
    Company_Password = models.CharField(max_length=30)

