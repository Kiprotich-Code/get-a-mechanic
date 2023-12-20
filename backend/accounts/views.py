from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'car_owner',
            user.save()
            return redirect('login')
        
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/register_user.html', context)

def register_mech(request):
    if request.method == 'POST':
        form = MechanicRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'mechanic'
            user.save()
            return redirect('login')
        
    else:
        form = MechanicRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/register_mech.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # redirect users based on roles
            if user.user_type == 'car_owner':
                return redirect('user_home')
            
            elif user.user_type == 'mechanic':
                return redirect('req_list')
            
            else:
                return redirect('user_home')
            
        else:
            return redirect('login')
        
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('base')