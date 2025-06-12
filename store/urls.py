from django.urls import path
from .views import (
    login_view, logout_view, home_view, store_home,
    electronics, apparel, books, signup_view,electronics_detail
)


urlpatterns = [
    path('', store_home, name='store-home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('electronics/<int:product_id>/', electronics_detail, name='electronics-detail'),

    path('electronics/', electronics, name='electronics'),
    path('apparel/', apparel, name='apparel'),
    path('books/', books, name='books'),  
     
]
