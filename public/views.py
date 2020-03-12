from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from farmers.models import products
# Create your views here.

def index(request):
	return render(request,"public/index.html")
def shop(request):
	current_user = request.user
	product=products.objects.filter(isactive=True)
	return render(request,"public/shop.html",{'product':product})
def about(request):
	return render(request,"public/about.html")
def contact(request):
	return render(request,"public/contact.html")
def cart(request):
	return render(request,"public/cart.html")
def checkout(request):
	return render(request,"public/checkout.html")
def wishlist(request):
	return render(request,"public/wishlist.html")
def product(request):
	pid = request.GET['id']
	product=products.objects.filter(id=pid)
	return render(request,"public/product.html",{'product':product})
def ourfarmers(request):
	return render(request,"public/ourfarmers.html")
def farmerdetails(request):
	return render(request,"public/ourfarmers_details.html")

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
			return redirect('/login')
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
		return redirect('/login')
	else:
		return render(request,"public/signup.html")