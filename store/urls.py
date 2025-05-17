from django.urls import path
from .views import store_home, electronics, apparel, books

urlpatterns = [
    path('', store_home, name='store-home'),
    path('electronics/', electronics, name='electronics'),
    path('apparel/', apparel, name='apparel'),
    path('books/', books, name='books'),
]
