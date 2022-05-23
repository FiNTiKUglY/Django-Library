from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import SignUpForm, LogInForm
from django.contrib.auth import login, logout


def index(request):
    books = Book.objects.all()
    return render(request, 'list.html', {'books': books})


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def log_in(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('')
    if request.method == 'POST':
        form = LogInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('')
    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form})

