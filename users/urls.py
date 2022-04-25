from django import contrib
from django import urls
from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [ 
    path('login/', views.LoginUser, name= 'login'),
    path('logout/', views.LogOutUser, name='logout'),
    path('register/', views.RegisterUser, name='register'),
]