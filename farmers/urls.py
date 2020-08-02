from django.urls import path
from . import views


urlpatterns = [
    path(r'dash/', views.dash,name='farmers_dash'),
    path(r'orderdetails/', views.orderdetails,name='order_details'),
    path(r'markdelivered/', views.markdelivered,name='mark_as_delivered'),
    path(r'orders/', views.orders,name='product_orders'),
    path(r'ordercount/', views.ordercount,name='order_count'),
    path(r'productdetails/',views.productdetails, name='productdetails'),
    path(r'editproduct/',views.editproduct, name='editproduct'),
    path(r'deleteproduct/',views.deleteproduct, name='deleteproduct'),
    path(r'markproduct/',views.markproduct, name='markproduct'),
    path(r'addproduct/', views.addproduct,name='farmers_addproduct'),
    path(r'login/', views.login,name='farmers_login'),
	path(r'logout/', views.logout,name='farmers_logout'),
    path(r'signup/', views.signup,name='farmers_signup'),
    path(r'orderhistory/', views.orderhistory,name='order_history'),
    path(r'invoice/', views.invoice,name='invoice'),
]