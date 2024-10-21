from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class tbl_Scrap(models.Model):
    Scrap_Category=models.CharField(max_length=50)
    Scrap_Quantity=models.CharField(max_length=50)
    Scrap_Description=models.CharField(max_length=50)
    Scrap_Price=models.CharField(max_length=50)
    Scrap_Photo=models.FileField(upload_to="Assets/Scrap/Photo/")
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    User=models.ForeignKey(tbl_user,on_delete=models.SET_NULL, null=True)
    Shop=models.ForeignKey(tbl_newShop,on_delete=models.SET_NULL, null=True)
    scarp_status = models.IntegerField(default=0)



class tbl_Complaint(models.Model):
    Complaint_Title=models.CharField(max_length=50)
    Complaint_Content=models.CharField(max_length=100)
    Complaint_Date=models.DateField(auto_now_add=True)
    Complaint_Replay=models.CharField(max_length=100)
    Complaint_Status=models.IntegerField(default=0)
    User=models.ForeignKey(tbl_user,on_delete=models.SET_NULL, null=True)
    Company=models.ForeignKey(tbl_company,on_delete=models.SET_NULL, null=True)
    Shop=models.ForeignKey(tbl_newShop,on_delete=models.SET_NULL, null=True)
    




class tbl_FeedBack(models.Model):
    Feedback_Content=models.CharField(max_length=50)
    Feedback_Date=models.DateField(auto_now_add=True)
    User=models.ForeignKey(tbl_user,on_delete=models.SET_NULL, null=True)
    Shop=models.ForeignKey(tbl_newShop,on_delete=models.SET_NULL, null=True)
    Company=models.ForeignKey(tbl_company,on_delete=models.SET_NULL, null=True)
    