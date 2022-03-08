
from django.urls import path
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm

from django.core.mail import send_mail


# Create your views here.


def home(request):
    return render(request, 'home.html')


def welcome(request):
    return render(request, 'welcome.html')


def contact(request):
    return render(request,  'contact.html')


def adventure(request):
    return render(request, 'adventure.html')


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('welcome')

    context = {
        'form': form,
    }
    return render(request, "register.html", context)


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('adventure')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def ocean(request):
    return render(request, 'ocean.html')


def send_gmail(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        print(firstname, lastname, email, subject)

        send_mail(

            email,
            subject,
            'from@mail.com',
            ['to@mail.com'],
            fail_silently=False,
        )

        return HttpResponseRedirect(reverse('contact'))
    else:
        return HttpResponse('Invalid request')
