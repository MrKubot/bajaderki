from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def unauth(response):
    return render(response, 'register/unauth.html')

def register(response):

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')
    else:
        form = RegisterForm()

    return render(response, 'register/register.html', {'form': form})

def login(response):

    if response.method == "POST":
        username = response.POST['username']
        password = response.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            return redirect('/')

    return render(response, 'registration/login.html', {})