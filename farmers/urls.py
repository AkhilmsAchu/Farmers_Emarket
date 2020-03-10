from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login', views.login,name='farmers_login'),
	path('logout', views.logout,name='farmers_logout'),
    path('signup', views.signup,name='farmers_signup'),
]