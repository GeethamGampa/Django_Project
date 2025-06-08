from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout 
import requests


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



def external_books_api(request):
    if request.method == 'POST':
        user_input = request.POST.get('title')
        url = 'https://stephen-king-api.onrender.com/api/books'
        response = requests.get(url)

        if response.status_code == 200:
            result = response.json()
            search_dict = {
                0: "carrie", 1: "salem's Lot", 2: "the shining", 3: "rage",
                4: "The Stand", 5: "The Long Walk", 6: "The Dead Zone", 7: "Firestarter",
                8: "Roadwork", 9: "Cujo", 10: "The Running Man", 11: "The Dark Tower",
                12: "Christine ", 13: "Pet Sematary", 14: "Cycle of the Werewolf",
                15: "The Talisman", 16: "The Eyes of the Dragon", 17: "Thinner",
                18: "It", 19: "The Dark Tower II: The Drawing of the Three", 20: "Misery"
            }

            for k, v in search_dict.items():
                if v.lower().strip() == user_input.lower().strip():
                    publisher = result['data'][k]['Publisher']
                    isbn = result['data'][k]['ISBN']
                    return render(request, 'api_result.html', {
                        'title': v,
                        'publisher': publisher,
                        'isbn': isbn
                    })

        return render(request, 'api_result.html', {'error': 'Book not found or API error'})

    return render(request, 'api_form.html')
