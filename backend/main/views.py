from django.shortcuts import render, redirect
from .forms import RequestMechForm
from django.views import generic
from .models import RequestMech

# Create your views here.
def base(request):
    return render(request, 'base.html')

def user_home(request):
    return render(request, 'car_owners/user_home.html')

# Car-owner views
def request_mech(request):
    if request.method == 'POST':
        form = RequestMechForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('req_list')
        
    else:
        form = RequestMechForm()

    context = {'form': form}
    return render(request, 'car_owners/request_mech.html', context)

class ReqList(generic.ListView):
    model = RequestMech
    template_name = 'car_owners/req_list.html'
    context_object_name = 'requests'

class ReqDetails(generic.DetailView):
    model = RequestMech
    template_name = 'car_owners/req_detail.html'
    context_object_name = 'request'
    