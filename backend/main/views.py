from django.shortcuts import render, redirect
from .forms import RequestMechForm

# Create your views here.
def base(request):
    return render(request, 'base.html')

# Car-owner request mech 
def request_mech(request):
    if request.method == 'POST':
        form = RequestMechForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        
    else:
        form = RequestMechForm()

    context = {'form': form}
    return render(request, 'car_owners/request_mech.html', context)