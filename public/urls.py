from django.urls import path
from . import views

urlpatterns = [
	path('farmerdetails', views.farmerdetails,name='farmerdetails'),
	path('ourfarmers', views.ourfarmers,name='ourfarmers'),
	path('product', views.product,name='product'),
	path('wishlist', views.wishlist,name='wishlist'),
	path('checkout', views.checkout,name='checkout'),
	path('cart', views.cart,name='cart'),
	path('about', views.about,name='about'),
	path('contact', views.contact,name='contact'),
    path('index', views.index,name='index'),
    path('', views.index,name='index'),
    path('shop', views.shop,name='shop'),
    path('login', views.login,name='user_login'),
	path('logout', views.logout,name='user_logout'),
    path('signup', views.signup,name='user_signup'),
]