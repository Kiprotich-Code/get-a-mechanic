from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.profile.is_first_login:
                update_profile_url = reverse('update_profile')
                return redirect(update_profile_url)
            
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


# view for profile 
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            frm = form.save(commit=False)
            request.user.profile.is_first_login = False
            frm.save()

            if request.user.user_type == 'mechanic':
                return redirect('req_list')
            
            else:
                return redirect('user_home')
            
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/update_profile.html', {'form': form})

def view_profile(request, user_id):
    user = CustomUser.objects.get(id=user_id)

    context = {
        'user': user
    }
    return render(request, 'accounts/view_profile.html', context)


