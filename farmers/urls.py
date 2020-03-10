from django.urls import path
from . import views

urlpatterns = [
    path('dash', views.dash,name='farmers_dash'),
    path('login', views.login,name='farmers_login'),
	path('logout', views.logout,name='farmers_logout'),
    path('signup', views.signup,name='farmers_signup'),
]