# Django_Project
## E-Commerce Website
 

**Esha** : creating a repo, created a database and a html page

**Geetham** : created a logic in urls.py and views.py, configuring in settings.py


**Step-1**: Created a repository named Django_project

**Step-2**: Created a virtual environment named Myenv

```bash
python -m venv Myenv
```

**Step-3**: Activated the virtual environment

```bash
Myenv\Scripts\activate
```

**Step-4**: Installed Django inside the virtual environment
 ```bash
pip install django
```
**Step-5**: Created a Django project named ECommerce
 ```bash
django-admin startproject ECommerce
```
**Step-6**: Created a Django app inside the project named store
 ```bash
python manage.py startapp store
```
**Step-7**: Added the store app to INSTALLED_APPS in ECommerce/settings.py
 ```bash
INSTALLED_APPS = [
    # ... other apps ...
    'store',
]
```
**Step-8**: Created basic views in store/views.py for electronics, apparel, and books pages
 ```bash
from django.http import HttpResponse

def electronics(request):
    return HttpResponse("List of Electronics Products")

def apparel(request):
    return HttpResponse("List of Apparel Products")

def books(request):
    return HttpResponse("List of Books")
```
**Step-9**: Created the store_home view to render an HTML template in store/views.py
 ```bash
from django.template import loader
from django.http import HttpResponse

def store_home(request):
    template = loader.get_template('store_home.html')
    return HttpResponse(template.render())
```
**Step-10**: Created the HTML template file store_home.html inside store/templates/
```bash
Example content of store_home.html:
<h1>Welcome to Store Home Page!</h1>
```
**Step-11**: Created a urls.py file inside the store app with URL patterns
 ```bash
from django.urls import path
from .views import store_home, electronics, apparel, books

urlpatterns = [
    path('', store_home, name='store-home'),
    path('electronics/', electronics, name='electronics'),
    path('apparel/', apparel, name='apparel'),
    path('books/', books, name='books'),
]
```
**Step-12**: Included store app URLs in the main project ECommerce/urls.py
 ```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
]
```
**Step-13**: Ran the development server
 ```bash
python manage.py runserver
```
**Step-14**: Opened browser and tested the URLs:
```bash
http://127.0.0.1:8000/store/ → Show the store home page (renders store_home.html)

http://127.0.0.1:8000/store/electronics/ → Shows "List of Electronics Products"

http://127.0.0.1:8000/store/apparel/ → Shows "List of Apparel Products"

http://127.0.0.1:8000/store/books/ → Shows "List of Books"
```
**Step-15**: Created models in store/models.py to store product info
 ```bash
from django.db import models

class Electronics(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()

class Apparel(models.Model):
    product_name = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    price = models.FloatField()

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.FloatField()
    genre = models.CharField(max_length=100)
```
**Step-16**: Made migrations to create database tables from models
```bash
python manage.py makemigrations
python manage.py migrate
```

