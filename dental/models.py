from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    
    genderChoices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    
    last_name = models.CharField(max_length=55, null=True)
    first_name = models.CharField(max_length=55, null=True)
    middle_name = models.CharField(max_length=55, null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=1, choices=genderChoices)
    address = models.CharField(max_length=55, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.last_name
    


class Service(models.Model):
    image = models.FileField(upload_to="services", null=True)
    name = models.CharField(max_length=55, null=True)
    description = models.TextField(max_length=255, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    date = models.DateField(null=True)
    patient = models.CharField(max_length=55, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.patient
    
    
class Payment(models.Model):
    image = models.FileField(upload_to="payments", null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    ref_number = models.PositiveIntegerField(null=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.ref_number

class Category(models.Model):
    name = models.CharField(max_length=55, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name