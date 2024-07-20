"""
URL configuration for python242 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.index1,name='index'),
    path('',views.index1,name='index'),
    path('temp/',views.register,name='temp'),
    path('login/',views.login,name='login'),
    path('temp2/',views.register1,name='temp2'),
    path('profile/',views.profile,name='profile'),
    path('updateprofile/',views.updateprofile,name='updateprofile'),
    path('stafflogin/',views.stafflogin,name='stafflogin'),
    path('indexstaff/',views.index2,name='indexstaff'),
    path('userlist/',views.userlist,name='userlist'),
    path('userstafflist/',views.userstafflist,name='userstafflist'),
    path('delete1/<int:id>',views.delete1,name='delete1'),
    path('delete2/<int:id>',views.delete2,name='delete2'),
    path('product/',views.registerproduct,name='product'),
    path('productlist/',views.productlist,name='productlist'),
    path('delete3/<int:id>',views.delete3,name='delete3'),
    path('adminindex/',views.index3,name='adminindex'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('search/',views.search,name='search'),
    path('cart/<int:id>',views.addcart,name='cart'),
    path('addcart2/',views.addcart2,name='addcart2'),
    path('productlist2/',views.productlist2,name='productlist2'),
    path('cartlist/',views.cartlist,name='cartlist'),
    path('delete4/<int:id>',views.delete4,name='delete4'),
]
