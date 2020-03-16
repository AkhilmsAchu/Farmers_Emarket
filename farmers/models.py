from django.db import models
from django.contrib.auth.models import User
# Create your models here.

ptypes = (
    ('Vegetables','Vegetables'),
    ('Products', 'Products'),
    ('Dried','Dried'),
    ('Fruits','Fruits')
)
class products(models.Model):
	pname = models.CharField(max_length=100)
	ptype = models.CharField(max_length=10, choices=ptypes, default='Vegetables')
	description = models.TextField()
	stock = models.IntegerField()
	price  =models.IntegerField()
	img = models.ImageField(upload_to='products/pics')
	offer = models.BooleanField(default=False)
	isactive = models.BooleanField(default=True) 
	offerprice = models.IntegerField(blank=True,null=True)
	created_at = models.DateField(auto_now_add=True)
	owner = models.ForeignKey(User,default=None,on_delete=models.DO_NOTHING)#for now to pass form validation,will remove later
