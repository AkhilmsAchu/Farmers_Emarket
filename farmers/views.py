
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import products
from django.forms import ModelForm
from public.models import cart, userProfile, wishlist, orderDetails, check_product_stock, reviewDetails
from django.views.generic import View
from Farmers_Emarket.utils import render_to_pdf
#from farmers.models import Article
# Create your views here.

class AddProductForm(ModelForm):
    class Meta:
        model = products
        fields = ['pname','ptype','description', 'stock', 'price', 'img', 'offer','offerprice']

class EditProductForm(ModelForm):
	class Meta:
	    model = products
	    fields = ['pname','ptype','description', 'stock', 'isactive', 'price', 'img', 'offer','offerprice']

def invoice(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
	oid = request.GET['id']
	orderlist=None
	try:
		orderlist=orderDetails.objects.get(productid__owner=request.user.id,status=True,id=oid)
	except orderDetails.DoesNotExist:
		orderlist = None
		print("nome")

	data={'pname':orderlist.productid.pname,
	'fname':orderlist.productid.owner.first_name,
	'qty':orderlist.quantity,
	'rate':orderlist.productid.price,
	'date':orderlist.date,
	'uaddress':orderlist.address,
	'paymode':orderlist.paymode,
	'uname':orderlist.userid.first_name,
	'id':orderlist.id,
	'total':int(orderlist.quantity)*int(orderlist.productid.price)
	}
	pdf = render_to_pdf('pdf/invoice.html',data)
	return HttpResponse(pdf, content_type='application/pdf')

def orderdetails(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
	oid = request.GET['id']
	try:
		orderlist=orderDetails.objects.filter(productid__owner=request.user.id,id=oid)
	except orderlist.DoesNotExist:
		orderlist = None
	return render(request,"farmers/orderdetails.html",{'orderlist':orderlist})

def dash(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
	current_user = request.user
	product=products.objects.filter(owner=request.user)
	return render(request,"farmers/dashboard.html",{'product':product})

def orderhistory(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
	try:
		orderlist=orderDetails.objects.filter(productid__owner=request.user.id,status=True)
	except orderlist.DoesNotExist:
		orderlist = None
	return render(request,"farmers/orderhistory.html",{'orderlist':orderlist})

def orders(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
	try:
		orderlist=orderDetails.objects.filter(productid__owner=request.user.id,status=False)
	except orderlist.DoesNotExist:
		orderlist = None
	return render(request,"farmers/orders.html",{'orderlist':orderlist})


def markdelivered(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
	oid = request.GET['id']
	try:
		orderlist=orderDetails.objects.get(productid__owner=request.user.id,status=False,id=oid)
	except orderDetails.DoesNotExist:
		orderlist = None
	if orderlist:
		orderlist.status = True
		orderlist.save()
		return HttpResponse('Marked as Delivered')
	else:
		return HttpResponse('Something went wrong, TryAgain')

def ordercount(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
	try:
		orderlist=orderDetails.objects.filter(productid__owner=request.user.id,status=False)
	except orderlist.DoesNotExist:
		orderlist = None
	if orderlist:
		return HttpResponse(len(orderlist))
	else:
		return HttpResponse('0')


def productdetails(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
	current_user = request.user
	pid = request.GET['id']
	product=products.objects.filter(owner=request.user,id=pid)
	tstar=0
	soldcount=0
	try:
		chkreview=reviewDetails.objects.filter(productid=pid)
		for rev in chkreview:
			tstar+=rev.stars
	except reviewDetails.DoesNotExist:
		chkreview = None
	try:
		rating=tstar/chkreview.count()
	except :
		rating=0.0
	half=rating.is_integer()
	if half:
		nostars=5-int(rating)
	else:
		nostars=4-int(rating)
	if not request.user.is_anonymous:
		try:
			soldlist=orderDetails.objects.filter(status=True,productid_id=pid)
			for sold in soldlist:
				soldcount+=sold.quantity
		except orderDetails.DoesNotExist:
			orderlist=None
	return render(request,"farmers/productdetails.html",{'soldcount':soldcount,'chkreview':chkreview,'product':product,'trate':rating,'soldcount':soldcount,'nostars':nostars,'half':half})

def addproduct(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
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
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
	pid = request.GET['id']
	if request.method == 'POST':
		current=products.objects.get(id=pid)
		form = EditProductForm(request.POST,request.FILES or None,instance=current)
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
			form = EditProductForm(initial={'pname': pro.pname,'ptype': pro.ptype,'description': pro.description,'stock': pro.stock,'isactive':pro.isactive,'price': pro.price,'img': pro.img,'offer': pro.offer,'offerprice': pro.offerprice})
			context={
			'form':form
			}
		return render(request,"farmers/addproduct.html",context)

def deleteproduct(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
	pid = request.GET['id']
	try:
		product=products.objects.filter(owner=request.user,id=pid)
	except products.DoesNotExist:
		product = None
	if product:
		try:
			product.delete()
			return HttpResponse('Product Removed')
		except:
			return HttpResponse('Something went wrong, TryAgain')
	else:
		return HttpResponse('No such Product')

def markproduct(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	elif request.user.userprofile.ismerchant==False:
		return redirect('/')
	pid = request.GET['id']
	opt = request.GET['type']
	try:
		product=products.objects.get(owner=request.user,id=pid)
	except products.DoesNotExist:
		product = None
	if product:
		if opt=="sold":
			product.isactive=False
			product.save()
			return HttpResponse('Product Marked as SOLD')
		else:
			product.isactive=True
			product.save()
			return HttpResponse('Product Marked as UNSOLD')
	else:
		return HttpResponse('something wrong, please try again')

def logout(request):
	if request.user.is_anonymous:
		return redirect('/farmers/login')
	auth.logout(request)
	return render(request,"farmers/login.html")

def login(request):
	if not request.user.is_anonymous:
		return redirect('/farmers/dash')
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
	if not request.user.is_anonymous:
		return redirect('/farmers/dash')
	if request.method == 'POST':
		try:
			first_name=request.POST['first_name']
			last_name=request.POST['last_name']
			email=request.POST['email']
			password=request.POST['password']
			username=request.POST['email']
			state=request.POST['state']
			house=request.POST['house']
			town=request.POST['town']
			pincode=request.POST['pincode']
			phone=request.POST['phone']
			description=request.POST['description']
			img=request.FILES['image']
			license_no=request.POST['license_no']
			manufacture_code=request.POST['manufacture_code']
			try:
				user =User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
				userp=userProfile.objects.create(user=user,state=state,house=house,town=town,pincode=pincode,phone=phone,ismerchant=True,description=description,img=img,license_no=license_no,manufacture_code=manufacture_code)
				userp.save()
				print('created')
			except Exception as e:
				if 'unique constraint' in str(e):
					return render(request,"farmers/signup.html",{'msg':"username/email already taken"})
				return render(request,"farmers/signup.html",{'msg':e})
		except:
			print("something went wrong")
			return render(request,"farmers/signup.html",{'msg':"fill all the fields"})
		return redirect('/farmers/login')
	else:
		return render(request,"farmers/signup.html")