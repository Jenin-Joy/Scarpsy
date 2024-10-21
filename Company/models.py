from django.db import models
from Guest.models import tbl_company
from Guest.models import tbl_newShop
from User.models import tbl_Scrap

# Create your models here.
class tbl_companybooking(models.Model):
    companybooking_date = models.DateField(auto_now_add=True)
    companybooking_status = models.IntegerField(default=0)
    company = models.ForeignKey(tbl_company, on_delete=models.CASCADE)
    scarp = models.ForeignKey(tbl_Scrap, on_delete=models.CASCADE)

class tbl_product(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.CharField(max_length=30)
    product_photo = models.FileField(upload_to="Assets/Company/Product/")
    company = models.ForeignKey(tbl_company, on_delete=models.CASCADE)

class tbl_stock(models.Model):
    stock = models.CharField(max_length=30)
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)

class tbl_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    booking_amount = models.CharField(max_length=30)
    booking_status = models.IntegerField(default=0)
    company = models.ForeignKey(tbl_company, on_delete=models.CASCADE)

class tbl_cart(models.Model):
    cart_qty = models.IntegerField(default=1)
    cart_status = models.IntegerField(default=0)
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_booking, on_delete=models.CASCADE)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=500)
    user_review=models.CharField(max_length=500)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)