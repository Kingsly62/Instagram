from instagram import views
from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    # path('logout', views.logout, name='logout')
    path('login', views.login, name='login'),
]
