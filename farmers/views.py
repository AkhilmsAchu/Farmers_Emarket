from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.

def dash(request):
	return render(request,"farmers/dashboard.html")

def logout(request):
	auth.logout(request)
	return redirect('/')

def login(request):
	if request.method == 'POST':
		password=request.POST['password']
		username=request.POST['username']
		is_merchant=True
		user=auth.authenticate(is_merchant='true',username=username,password=password)
		if user is not None:
			auth.login(request,user)
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
		return render(request,"farmers/login.html")
	else:
		return render(request,"farmers/signup.html")