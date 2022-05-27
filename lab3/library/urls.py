from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name=''),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('orders/', views.OrderViewer.as_view(), name='orders'),
    path('book/<int:id>', views.BookViewer.as_view(), name='book'),
    path('remove/<int:id1>/<int:id2>', views.RemoveBook.as_view(), name='remove'),
    path('mail/<int:id>', views.MailCreator.as_view(), name='mail'),
    path('book/<int:id>/add/', views.AddInOrder.as_view(), name='add')
]
