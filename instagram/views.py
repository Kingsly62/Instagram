
from django.urls import path
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):

    return render(request, ' contact.html')


def adventure(request):
    return render(request, 'adventure.html')


def register(request):

    return render(request, 'register.html')


def ocean(request):
    return render(request, 'ocean.html')


@login_required
def login(reqiured):
    return render(reqiured, 'login.html')


@login_required
def profile(request):
    return render(request, "profile.html")
