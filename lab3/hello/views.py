from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'list.html', {'books': books})
