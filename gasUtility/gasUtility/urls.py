"""
URL configuration for gasUtility project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from services_requests.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/', submit_request, name='submit_request'),
    path('request_list/', request_list, name='request_list'),
    path('manage_requests/', manage_requests, name='manage_requests'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='services_requests/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
]
