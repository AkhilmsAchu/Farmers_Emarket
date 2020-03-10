from django.db import models

# Create your models here.
class products(models.Model):
	pname = models.CharField(max_length=100)
	ptype = models.CharField(max_length=100)
	description = models.TextField()
	stock = models.IntegerField()
	price  =models.IntegerField()
	img = models.ImageField(upload_to='products/pics')
	offer = models.BooleanField(default=False)
	offerprice = models.IntegerField()
	created_at = models.DateField(auto_now_add=True)
	userid = models.CharField(max_length=100)