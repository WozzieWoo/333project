from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),        # http://localhost:8000/
    path('index/', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('comunity/', views.comunity, name='comunity'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('error/', views.prueba_error, name='prueba_error'),
]
