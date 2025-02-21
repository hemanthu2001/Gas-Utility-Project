from django.db import models
from django.contrib.auth.models import User


class ServiceRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('new', 'New Connection'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/' , blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer.username} - {self.get_request_type_display()} - {self.status}'
    
