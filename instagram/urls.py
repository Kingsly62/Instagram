from instagram import views
from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('adventure', views.adventure, name='adventure'),
    path('register', views.register_view, name='register'),
    # path('logout', views.logout, name='logout')
    path('login', views.login_view, name='login'),
    path('ocean', views.ocean, name='ocean')
]
