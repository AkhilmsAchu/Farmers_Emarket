from django.db import models
from django.contrib.auth.models import User
from farmers.models import products
from django.db.models.signals import post_save
# Create your models here.


class cart(models.Model):
	userid = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	productid = models.ForeignKey(products,default=None,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

class userProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	state = models.CharField(max_length=200,default='')
	house = models.CharField(max_length=200,default='')
	town = models.CharField(max_length=200,default='')
	pincode = models.CharField(max_length=12,default='')
	phone = models.CharField(max_length=12,default='')
	ismerchant = models.BooleanField(default=False)
	description = models.CharField(max_length=200,default='')
	img = models.ImageField(upload_to='farmers/pics', default='default.jpg')
	isactive = models.BooleanField(default=True)
	license_no = models.CharField(max_length=20,default='')
	manufacture_code = models.CharField(max_length=20,default='')

	def __str__(self):
		return self.user.username
		
def check_product_stock(pid):
	product=products.objects.get(id=pid)
	if product.stock==0:
		product.isactive=False
		product.save()
		print("marked inactive")

class wishlist(models.Model):
	userid = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	productid = models.ForeignKey(products,default=None,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

class orderDetails(models.Model):
	userid = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	productid = models.ForeignKey(products,default=None,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	date = models.DateTimeField(auto_now_add=True)
	address = models.TextField()
	status = models.BooleanField(default=False)
	paymode = models.CharField(max_length=20,default=None)

class reviewDetails(models.Model):
	userid = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	productid = models.ForeignKey(products,default=None,on_delete=models.CASCADE)
	stars = models.IntegerField(default=1)
	review = models.CharField(max_length=200,default='')