from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ServiceRequestForm
from .models import ServiceRequest


@login_required
def submit_list(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()

    return render(request, 'services_requests/request_list.html', {'form': form})


@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'services_requests/request_list.html', {'requests': requests})



@staff_member_required
def manage_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'services_requests/manage_requests.html', {'requests': requests})

