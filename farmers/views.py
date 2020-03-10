from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import products
from django.forms import ModelForm
#from farmers.models import Article
# Create your views here.
class AddProductForm(ModelForm):
    class Meta:
        model = products
        fields = ['pname','ptype','description', 'stock', 'price', 'img', 'offer','offerprice']
def dash(request):
	return render(request,"farmers/dashboard.html")

def addproduct(request):
	form = AddProductForm(request.POST,request.FILES or None)
	context={
		'form':form
		}
	if request.method == 'POST':
		
		if form.is_valid():
			form.save()
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