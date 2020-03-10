from django.db import models

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
	offerprice = models.IntegerField(blank=True,null=True)
	created_at = models.DateField(auto_now_add=True)
	userid = models.CharField(max_length=100,blank=True,null=True)#for now to pass form validation,will remove later