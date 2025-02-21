from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ServiceRequestForm
from .models import ServiceRequest


def home(request):
    return render(request, 'services_requests/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('submit_request')
    else:
        form = UserCreationForm()
    return render(request, 'services_requests/register.html', {'form': form})


@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()

    return render(request, 'services_requests/submit_request.html', {'form': form})


@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'services_requests/request_list.html', {'requests': requests})



@staff_member_required
def manage_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'services_requests/manage_requests.html', {'requests': requests})

