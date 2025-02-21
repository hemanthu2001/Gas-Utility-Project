from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ServiceRequestSerializer
from .models import ServiceRequest


class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        if self.request.user.is_staff:
            return ServiceRequest.objects.all()
        return ServiceRequest.objects.filter(customer=self.request.user)
    

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

        