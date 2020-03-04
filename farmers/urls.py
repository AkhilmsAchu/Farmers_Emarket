from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name='farmers_login'),
    path('login', views.login,name='farmers_login'),
    path('signup', views.signup,name='farmers_signup'),
]