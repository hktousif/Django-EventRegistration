from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def signup_view(request):
    registered = False
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            user = login_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            if user is not None:
                login(request, user)
            return redirect('/')
    context = {'login_form': UserForm(), 'registered': registered}
    return render(request, "signup.html", context)


def profile_view(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = User
            if 'Profile_Picture' in request.FILES:
                profile.Profile_Picture('Profile_Picture')
            profile.save()
    context = {'profile_form': UserProfileForm()}
    return render(request, "profile.html", context)


def logout_view(request):
    auth.logout(request)
    return redirect('/')


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid Username or Password')
                return redirect('/user/login')
    else:
        context = {'form': form}
        return render(request, 'login.html', context)
