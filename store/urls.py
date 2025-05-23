from django.urls import path
from .views import store_home, electronics, apparel, books, signup_view, login_view
from .views import logout_view

urlpatterns = [
    path('', store_home, name='store-home'),
    path('electronics/', electronics, name='electronics'),
    path('store_home/', store_home, name='store-home-alias'),
    path('apparel/', apparel, name='apparel'),
    path('books/', books, name='books'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]
