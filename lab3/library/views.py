from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Order, Mail
from .forms import SignUpForm, LogInForm, MailForm
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


def orders(request):
    active_order = Order.objects.filter(user__username=request.user.get_username(), is_active=True).first()
    mails = Mail.objects.filter(order__user__username=request.user.get_username())
    return render(request, 'orders.html', {'active_order': active_order, 'mails': mails})


def add_in_order(request, id):
    order = Order.objects.filter(is_active=True).first()
    if order is None:
        order = Order()
        order.user = request.user
        order.is_active = True
        order.save()
    order.book.add(Book.objects.get(id=id))
    return redirect('orders')


def remove_book(request, id1, id2):
    order = Order.objects.get(id=id1)
    order.book.remove(Book.objects.get(id=id2))
    return redirect('orders')


def book(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book.html', {'book': book})


def mail(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        form = MailForm(data=request.POST)
        if form.is_valid():
            order.is_active = False
            order.save()
            mail = Mail()
            mail.name = form.cleaned_data['name']
            mail.surname = form.cleaned_data['surname']
            mail.adress = form.cleaned_data['adress']
            mail.index = form.cleaned_data['index']
            mail.order = order
            mail.save()
            return redirect('orders')
    else:
        form = MailForm()
    return render(request, 'mail.html', {'form': form})

