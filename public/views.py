from django.shortcuts import render
from django.http import HttpResponse
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