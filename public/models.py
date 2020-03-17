from django.db import models
from django.contrib.auth.models import User
from farmers.models import products
# Create your models here.


class cart(models.Model):
	userid = models.ForeignKey(User,default=None,on_delete=models.DO_NOTHING)
	productid = models.ForeignKey(products,default=None,on_delete=models.DO_NOTHING)
	quantity = models.IntegerField(default=1)

class userProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	state = models.CharField(max_length=200)
	house = models.CharField(max_length=200)
	town = models.CharField(max_length=200)
	pincode = models.IntegerField()
	phone = models.CharField(max_length=12)
	ismerchant = models.BooleanField(default=False)
	description = models.CharField(max_length=200,default=None)
	img = models.ImageField(upload_to='farmers/pics',default=None)
	isactive = models.BooleanField(default=True)
	license_no = models.CharField(max_length=20,default=None)
	manufacture_code = models.CharField(max_length=20,default=None)

class wishlist(models.Model):
	userid = models.ForeignKey(User,default=None,on_delete=models.DO_NOTHING)
	productid = models.ForeignKey(products,default=None,on_delete=models.DO_NOTHING)
	quantity = models.IntegerField(default=1)