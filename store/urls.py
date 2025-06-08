from django.urls import path
from .views import login_view, logout_view, home_view, store_home, electronics, apparel, books, signup_view 
from .views import external_books_api

urlpatterns = [
    path('', store_home, name='store-home'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    
    path('', store_home, name='store-home'),
    path('electronics/', electronics, name='electronics'),
    path('apparel/', apparel, name='apparel'),
    path('books/', books, name='books'),
    path('external-books/', external_books_api, name='external-books'),


]
