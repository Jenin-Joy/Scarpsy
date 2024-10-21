from django.db import models
from Guest.models import tbl_newShop
from User.models import tbl_Scrap
# Create your models here.

class tbl_shopbooking(models.Model):
    shopbooking_date = models.DateField(auto_now_add=True)
    shopbooking_status = models.IntegerField(default=0)
    shop = models.ForeignKey(tbl_newShop, on_delete=models.CASCADE)
    scarp = models.ForeignKey(tbl_Scrap, on_delete=models.CASCADE)