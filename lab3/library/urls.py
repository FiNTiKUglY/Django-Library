from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('registration/', views.registration, name='registration'),
    path('login/', views.log_in, name='login')
]