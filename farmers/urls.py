from django.urls import path
from . import views


urlpatterns = [
    path(r'dash/', views.dash,name='farmers_dash'),
    path(r'orders/', views.orders,name='product_orders'),
    path(r'productdetails/',views.productdetails, name='productdetails'),
    path(r'editproduct/',views.editproduct, name='editproduct'),
    path(r'addproduct/', views.addproduct,name='farmers_addproduct'),
    path(r'login/', views.login,name='farmers_login'),
	path(r'logout/', views.logout,name='farmers_logout'),
    path(r'signup/', views.signup,name='farmers_signup'),
]