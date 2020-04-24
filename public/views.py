from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from farmers.models import products
from .models import cart, userProfile, wishlist, orderDetails, check_product_stock
from django.forms import ModelForm
from django.db import transaction
from django.db.models import F

# Create your views here.

class AddcartForm(ModelForm):
    class Meta:
        model = cart
        fields = ['userid','productid','quantity']

def orderhistory(request):
	try:
		orderlist=orderDetails.objects.filter(userid_id=request.user,status=True)
	except orderlist.DoesNotExist:
		orderlist = None
	return render(request,"public/orderhistory.html",{'orderlist':orderlist})

def removefromwish(request):
	
	pid = request.GET['id']
	product=products.objects.get(id=pid)
	try:
		chkwish=wishlist.objects.get(productid=pid,userid=request.user.id)
	except wishlist.DoesNotExist:
		chkwish = None
	if chkwish:
		try:
			chkwish.delete()
			return HttpResponse('Product Removed from Wishlist')
		except:
			return HttpResponse('Something went wrong, TryAgain')
	else:
		return HttpResponse('No such Product in Wishlist')

def addtowish(request):
	
	pid = request.GET['id']
	qty = request.GET['qty']
	product=products.objects.get(id=pid)
	try:
		chkwish=wishlist.objects.get(productid=pid,userid=request.user.id)
	except wishlist.DoesNotExist:
		chkwish = None
	if chkwish:
		return HttpResponse('Product already in Wishlist')
	else:
		instance = wishlist(userid=request.user,productid=product,quantity=qty)
		try:
			instance.save()
			return HttpResponse('Added to Wishlist')
		except:
			return HttpResponse('Something went wrong, TryAgain')

def cartcount(request):
	try:
		chkcart=cart.objects.filter(userid=request.user.id)
	except cart.DoesNotExist:
		chkcart = None
	if chkcart:
		return HttpResponse(len(chkcart))
	else:
		return HttpResponse('0')

def removefromcart(request):
	
	pid = request.GET['id']
	product=products.objects.get(id=pid)
	try:
		chkcart=cart.objects.get(productid=pid,userid=request.user.id)
	except cart.DoesNotExist:
		chkcart = None
	if chkcart:
		try:
			chkcart.delete()
			return HttpResponse('Product Removed from Cart')
		except:
			return HttpResponse('Something went wrong, TryAgain')
	else:
		return HttpResponse('No such Product in Cart')

def addtocart(request):
	
	pid = request.GET['id']
	qty = request.GET['qty']
	product=products.objects.get(id=pid)
	try:
		chkcart=cart.objects.get(productid=pid,userid=request.user.id)
	except cart.DoesNotExist:
		chkcart = None
	if chkcart:
		return HttpResponse('Product already in Cart')
	else:
		instance = cart(userid=request.user,productid=product,quantity=qty)
		try:
			instance.save()
			return HttpResponse('Added to Cart')
		except:
			return HttpResponse('Something went wrong, TryAgain')

def index(request):
	return render(request,"public/index.html")
def shop(request):
	try:
		cat = request.GET['cat']
	except:
		cat = 'All'	
	current_user = request.user
	product=products.objects.filter(isactive=True)
	return render(request,"public/shop.html",{'product':product,'cat':cat})
def about(request):
	return render(request,"public/about.html")
def contact(request):
	return render(request,"public/contact.html")

def viewcart(request):
	try:
		cartlist=cart.objects.filter(userid=request.user.id)
	except cart.DoesNotExist:
		cartlist = None
	total=0
	subtotal=[]
	if cartlist:
		for item in cartlist:
			if item.productid.offer:
				subtotal.append(item.productid.offerprice*item.quantity)
				total=total+item.productid.offerprice*item.quantity
			else:
				subtotal.append(item.productid.price*item.quantity)
				total=total+item.productid.price*item.quantity
	return render(request,"public/cart.html",{'cartlist':cartlist,'subtotal':subtotal,'total':total})


	return render(request,"public/cart.html")
def checkout(request):
	return render(request,"public/checkout.html")

def viewwishlist(request):
	try:
		wishlst=wishlist.objects.filter(userid=request.user.id)
	except wishlist.DoesNotExist:
		wishlst = None
	subtotal=[]
	if wishlst:
		for item in wishlst:
			if item.productid.offer:
				subtotal.append(item.productid.offerprice*item.quantity)
			else:
				subtotal.append(item.productid.price*item.quantity)
	return render(request,"public/wishlist.html",{'wishlist':wishlst,'subtotal':subtotal})

def product(request):
	pid = request.GET['id']
	product=products.objects.filter(id=pid)
	for pro in product:
		type=pro.ptype
	rproduct=products.objects.filter(ptype=type,isactive=True).exclude(id = pid)[:4]
	buyed = False
	if not request.user.is_anonymous:
		try:
			orderlist=orderDetails.objects.filter(userid_id=request.user,status=True,productid_id=pro)
		except orderDetails.DoesNotExist:
			orderlist=None
		if orderlist:
			buyed=True
	return render(request,"public/product.html",{'product':product,'rproduct':rproduct,'buyed':buyed})

def ourfarmers(request):
	farmers=User.objects.filter(userprofile__ismerchant=True)
	return render(request,"public/ourfarmers.html",{'farmers':farmers})


def farmerdetails(request):
	fid = request.GET['id']
	farmers=User.objects.filter(userprofile__ismerchant=True,id=fid)
	product=products.objects.filter(isactive=True,owner=fid)[:4]
	return render(request,"public/ourfarmers_details.html",{'farmers':farmers,'products':product})

def logout(request):
	auth.logout(request)
	return redirect('/')

def login(request):
	if request.method == 'POST':
		password=request.POST['password']
		username=request.POST['username']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else :
			return redirect('/plogin')
	else:
		return render(request,"public/login.html")
def signup(request):
	if request.method == 'POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		password=request.POST['password']
		username=request.POST['email']

		user =User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
		user.save();
		print('created')
		return redirect('/plogin')
	else:
		return render(request,"public/signup.html")

def orderstatus(request):
	user = request.user
	paymode=request.POST['optradio']
	flag=False
	address=user.first_name+user.last_name+","+user.userprofile.house+","+user.userprofile.town+","+user.userprofile.state+","+str(user.userprofile.pincode)+","+str(user.userprofile.phone)+","+user.email
	print(address)
	try:
		cartlist=cart.objects.filter(userid=request.user.id)
	except cart.DoesNotExist:
		cartlist = None
	if cartlist:
		with transaction.atomic():	
			for item in cartlist:
				product=products.objects.get(id=item.productid.id)
				instance = orderDetails(userid=request.user,productid=product,quantity=item.quantity,address=address,paymode=paymode)
				product.stock = F('stock')- item.quantity
				try:
					product.save()
					check_product_stock(product.id)
					instance.save()
					print("added to o list")
					#return HttpResponse('Added to Cart')
				except Exception as e:
					print(e)
					print("Something went wrong with ol, TryAgain")
					#return HttpResponse('Something went wrong, TryAgain')
			flag=True

	try:
		cartlist=cart.objects.filter(userid=request.user.id)
	except cart.DoesNotExist:
		cartlist = None
	if cartlist:
		with transaction.atomic():	
			for item in cartlist:
				try:
					item.delete()
					print("deleted from cart")
					#return HttpResponse('Added to Cart')
				except Exception as e:
					print(e)
					print("Something went wrong, TryAgain")
					#return HttpResponse('Something went wrong, TryAgain')
			flag=True

	if flag:
		return render(request,"public/order_status.html",{'status':flag})