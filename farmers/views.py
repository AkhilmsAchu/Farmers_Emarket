from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
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
		return redirect('/')
	else:
		return render(request,"farmers/signup.html")
		print('failed')