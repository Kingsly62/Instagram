
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


def register(request):
    if request.method == 'POST':
        name = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            user = User.objects.create_user(
                username=name, email=email, password=password1)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(
                request, 'Your account has been created! You are able to login')
            return redirect('login')
        else:
            messages.warning(request, 'Password Mismatching...!!!')
            return redirect('register')
    else:
        form = CreateUserForm()
        return render(request, "register.html", {'form': form})


def login(reqiured):
    return render(reqiured, 'login.html')


@login_required
def profile(request):
    return render(request, "profile.html")
