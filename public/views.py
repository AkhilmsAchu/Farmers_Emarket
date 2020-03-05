from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
	return render(request,"public/index.html")
def shop(request):
	return render(request,"public/shop.html")
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
	return render(request,"public/product.html")
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
		return redirect('/login')
	else:
		return render(request,"farmers/signup.html")