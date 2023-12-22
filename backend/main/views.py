from django.shortcuts import render, redirect
from .forms import RequestMechForm
from django.views import generic
from .models import RequestMech
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

# Create your views here.
def base(request):
    return render(request, 'base.html')

def user_home(request):
    return render(request, 'car_owners/user_home.html')

# Car-owner views
@login_required()
def request_mech(request, mech_id):
    if request.method == 'POST':
        form = RequestMechForm(request.POST)
        mechanic = CustomUser.objects.get(id=mech_id)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.car_owner = request.user
            frm.mech = mechanic
            frm.save()
            return redirect('user_home')
        
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

# Get a list of mechanics 
def mech_list(request):
    mechs = CustomUser.objects.filter(user_type='mechanic')
    context = {
        'mechs': mechs
    }
    return render(request, 'car_owners/mech_list.html', context)

