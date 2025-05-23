from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout 

def electronics(request):
    return HttpResponse("List of Electronics Products")

def apparel(request):
    return HttpResponse("List of Apparel Products")

def books(request):
    return HttpResponse("List of Books")

def store_home(request):
    template = loader.get_template('store_home.html')
    return HttpResponse(template.render())


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('store-home')  
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')   

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
    return redirect('store-home')