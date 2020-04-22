from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	path('removefromwish', views.removefromwish, name='removefromwish'),
	path('addtowish', views.addtowish, name='addtowish'),
	path('removefromcart', views.removefromcart, name='removefromcart'),
	path('cartcount', views.cartcount, name='cart_count'),
	path('addtocart', views.addtocart, name='cart_create'),
	path('farmerdetails', views.farmerdetails,name='farmerdetails'),
	path('ourfarmers', views.ourfarmers,name='ourfarmers'),
	path('product', views.product,name='product'),
	path('wishlist', views.viewwishlist,name='viewwishlist'),
	path('checkout', views.checkout,name='checkout'),
	path('cart', views.viewcart,name='cart'),
	path('about', views.about,name='about'),
	path('contact', views.contact,name='contact'),
    path('index', views.index,name='index'),
    path('', views.index,name='index'),
    path('shop', views.shop,name='shop'),
    path('plogin', views.login,name='user_login'),
	path('logout', views.logout,name='user_logout'),
    path('signup', views.signup,name='user_signup'),
    path('orderstatus', views.orderstatus,name='orderstatus'),
    path('orderhistory', views.orderhistory,name='order_shistory'),
]