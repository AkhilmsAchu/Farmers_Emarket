
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import products
from django.forms import ModelForm
from public.models import cart, userProfile, wishlist, orderDetails, check_product_stock
#from farmers.models import Article
# Create your views here.
class AddProductForm(ModelForm):
    class Meta:
        model = products
        fields = ['pname','ptype','description', 'stock', 'price', 'img', 'offer','offerprice']

class EditProductForm(ModelForm):
	class Meta:
	    model = products
	    fields = ['pname','ptype','description', 'stock', 'price', 'img', 'offer','offerprice']

def dash(request):
	current_user = request.user
	product=products.objects.filter(owner=request.user)
	return render(request,"farmers/dashboard.html",{'product':product})

def orders(request):
	try:
		orderlist=orderDetails.objects.filter(productid__owner=request.user.id,status=False)
	except orderlist.DoesNotExist:
		orderlist = None
	return render(request,"farmers/orders.html",{'orderlist':orderlist})


def markdelivered(request):
	pid = request.GET['id']
	try:
		orderlist=orderDetails.objects.get(productid__owner=request.user.id,status=False)
	except orderlist.DoesNotExist:
		orderlist = None
	if orderlist:
		orderlist.status = True
		orderlist.save()
		return HttpResponse('Marked as Delivered')
	else:
		return HttpResponse('Something went wrong, TryAgain')

def ordercount(request):
	try:
		orderlist=orderDetails.objects.filter(productid__owner=request.user.id,status=False)
	except orderlist.DoesNotExist:
		orderlist = None
	if orderlist:
		return HttpResponse(len(orderlist))
	else:
		return HttpResponse('0')


def productdetails(request):
	current_user = request.user
	pid = request.GET['id']
	product=products.objects.filter(owner=request.user,id=pid)
	return render(request,"farmers/productdetails.html",{'product':product})

def addproduct(request):
	current_user = request.user
	form = AddProductForm(request.POST,request.FILES or None)
	context={
		'form':form
		}
	if request.method == 'POST':
		
		if form.is_valid():
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save()
			return redirect(r'/farmers/dash/')
		else:
			form = AddProductForm(request.POST or None)
			context={
			'form':form
			}
			return render(request,"farmers/addproduct.html",context)
	else :
		form = AddProductForm()
		context={
		'form':form
		}
		return render(request,"farmers/addproduct.html",context)

def editproduct(request):
	pid = request.GET['id']
	if request.method == 'POST':
		current=products.objects.get(id=pid)
		form = AddProductForm(request.POST,request.FILES or None,instance=current)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save()
			return redirect(r'/farmers/dash')
		else:
			form = EditProductForm(request.POST,request.FILES or None)
			context={
			'form':form
			}
			return render(request,"farmers/editproduct.html",context)
	else :
		current_user = request.user
		product=products.objects.filter(owner=request.user,id=pid)
		for pro in product:
			form = EditProductForm(initial={'pname': pro.pname,'ptype': pro.ptype,'description': pro.description,'stock': pro.stock,'price': pro.price,'img': pro.img,'offer': pro.offer,'offerprice': pro.offerprice})
			context={
			'form':form
			}
		return render(request,"farmers/addproduct.html",context)


def logout(request):
	auth.logout(request)
	return render(request,"farmers/login.html")

def login(request):
	if request.method == 'POST':
		password=request.POST['password']
		username=request.POST['username']
		is_merchant=True
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			if user.userprofile.ismerchant==True:	
				return redirect('/farmers/dash')
			else:
				return redirect('/')

		else :
			return render(request,"farmers/login.html")
	else:
		return render(request,"farmers/login.html")
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
		return redirect('/farmers/login')
	else:
		return render(request,"farmers/signup.html")