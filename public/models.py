from django.db import models
from django.contrib.auth.models import User
from farmers.models import products
# Create your models here.


class cart(models.Model):
	userid = models.ForeignKey(User,default=None,on_delete=models.DO_NOTHING)
	productid = models.ForeignKey(products,default=None,on_delete=models.DO_NOTHING)
	quantity = models.IntegerField(default=1)