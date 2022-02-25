from tkinter import Widget
from turtle import RawTurtle
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import form_users_form
# Create your views here.


def home(request):
    print(request)
    return render(request, 'pages/home.html',)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin@g.c' and password == 'admin':
            return redirect('/user_details/')
        else:
            return render(request, 'pages/login.html', {'error': 'Invalid username or password'})
    return render(request, 'pages/login.html')


def signup(request):
    if request.method == 'POST':
        form = form_users_form(request.POST)
        if form.is_valid():
            print('valid')
            pass
        else:
            print('invalid')
            return render(request, 'pages/signup.html', {'form': form})
    return render(request, 'pages/signup.html')


# def register(request):

#     else:
#         form = form_users_form()
#     return render(request, 'pages/signup.html', {'form': form})


def user_details(request):
    return render(request, 'pages/user_details.html')
