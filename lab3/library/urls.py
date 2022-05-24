from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('registration/', views.registration, name='registration'),
    path('login/', views.log_in, name='login'),
    path('orders/', views.orders, name='orders'),
    path('book/<int:id>', views.book, name='book'),
    path('remove/<int:id1>/<int:id2>', views.remove_book, name='remove'),
    path('mail/<int:id>', views.mail, name='mail'),
    path('book/<int:id>/add/', views.add_in_order, name='add')
]
