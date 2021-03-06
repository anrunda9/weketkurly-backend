from django.contrib import admin
from django.urls    import path, include

urlpatterns = [
    path('users', include('users.urls')),
    path('orders', include('orders.urls')),
    path('products', include('products.urls')),
    path('home', include('promotion.urls'))
]
