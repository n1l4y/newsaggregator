from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from news.models import Category

def signup_view(request):
    AllCategories = Category.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home after sign-up
    else:
        form = UserCreationForm()
        
    return render(request, 'signup.html', {'form': form, 'AllCategories': AllCategories})

def login_view(request):
    AllCategories = Category.objects.all()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form, 'AllCategories': AllCategories})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')