from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout 

def store_home(request):
    return render(request, 'home.html')

def electronics(request):
    return render(request, 'electronics.html')

def apparel(request):
    return render(request, 'apparel.html')

def books(request):
    return render(request, 'books.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'pa$$w0rd':
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Account created successfully, now you can login')
        return redirect('login')
    return render(request, 'signup.html') 

def logout_view(request):
    logout(request)
    return redirect('login')