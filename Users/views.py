from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *


# Create your views here.
def signup_view(request):
    if request.method == 'POST' and request.POST['password'] == request.POST['password-repeat']:
        try:
            User.objects.get(username=request.POST['username'])
            return render(request, "signup.html", {'error': 'Username already exist'})
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['firstname'], email=request.POST['email'],
                                            password=request.POST['password'])
            auth.login(request, user)
            return redirect('/')
    return render(request, "signup.html")


def profile_view(request):
    return render(request, "profile.html")


def logout_view(request):
    auth.logout(request)
    return redirect('/')


def login_view(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': "Invalid username or password"})
    return render(request, 'login.html')
