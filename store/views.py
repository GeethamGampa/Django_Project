from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
import requests

def store_home(request):
    return render(request, 'home.html')

#=========================================================================#
def electronics(request):
    # URL to get electronics products from an external API (up to 100 items)
    url = 'https://dummyjson.com/products/category/electronics?limit=100'
    # Empty list to hold products we will show on the page
    products_list = []
    # Variable to store error messages, if any
    error = None

    try:
        resp = requests.get(url) # send an HTTP GET request to the API URL to get the products data.
        if resp.status_code == 200:
            all_products = resp.json().get('products', [])

            if request.method == 'POST':
                query = request.POST.get('query', '').strip().lower()
                products_list = [
                    p for p in all_products if query in p.get('title', '').lower()
                ]
                if not products_list:
                    error = "No electronics found for that search."
            else:
                # On GET, show all products
                products_list = all_products
        else:
            error = "Couldn't load electronics items."
    except Exception as e:
        error = f"Error: {e}"

    return render(request, 'electronics.html', {
        'products': products_list,
        'error': error,
    })


def electronics_detail(request, product_id):
    url = f'https://dummyjson.com/products/{product_id}'
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            product = resp.json()
            return render(request, 'electronics_detail.html', {'product': product})
        else:
            return render(request, 'electronics_detail.html', {'error': 'Product not found'})
    except Exception as e:
        return render(request, 'electronics_detail.html', {'error': f"Error: {e}"})

#=========================================================================#



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


def books(request):
    url = 'https://stephen-king-api.onrender.com/api/books'
    response = requests.get(url)
    books_list = []

    if response.status_code == 200:
        data = response.json()
        books_list = data.get('data', [])

    # If a book is searched via Details button
    if request.method == 'POST':
        searched_title = request.POST.get('search_title', '').strip().lower()
        for book in books_list:
            if book.get('Title', '').strip().lower() == searched_title:
                return render(request, 'book_detail.html', {
                    'title': book.get('Title'),
                    'publisher': book.get('Publisher'),
                    'isbn': book.get('ISBN')
                })
        return render(request, 'book_detail.html', {'error': 'Book not found'})

    return render(request, 'books.html', {'books': books_list})

def apparel(request):
       
    url = 'https://dummyjson.com/products/category/womens-dresses?limit=100'
    products_list = []
    error = None

    resp = requests.get(url)
    if resp.status_code == 200:
        all_products = resp.json().get('products', [])

        if request.method == 'POST':
            query = request.POST.get('query', '').strip().lower()
            products_list = [
                p for p in all_products
                if query in p.get('title', '').lower()
            ]
            if not products_list: 
                error = "No apparel found for that search."
        else:
            products_list = all_products
    else:
        error = "Couldn't load apparel items."

    return render(request, 'apparel.html', {
        'products': products_list,
        'error': error,
    })
