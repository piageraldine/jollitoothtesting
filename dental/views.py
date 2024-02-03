from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from . import views
from dental.models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
# Create your views here.



def home(request):
    
    services = Service.objects.all()
    context = {
        'services' : services
    }
    
    return render(request, 'pages/home.html', context)

def set_appointment(request):
    
    services = Service.objects.all()
    
    
    if request.method == 'POST':
        
        
        appointmentData = {
            'patient' : request.POST.get('patient'),
            'date' : request.POST.get('date'),
            'service' : request.POST.get('service')
        }
        

        service = Service.objects.filter(id=appointmentData['service']).first()
    
        Appointment.objects.create(patient=appointmentData['patient'], date=appointmentData['date'], service=service)
        
        return redirect(to='home')
    
    context = {
        'services' : services
    }
    
    return render(request, 'pages/Appointment/create.html', context)

def sign_in(request):
    if request.user.is_authenticated:
        return redirect(to="home")
    
    
    if request.method == 'POST':
        credential = {
            'username' : request.POST.get('username'),
            'password' : request.POST.get('password')
        }
        authenticate_user = authenticate(username=credential['username'], password=credential['password'])
        
        if authenticate_user is not None:
            login(request, authenticate_user)
            
            return redirect(to="home")
    
    return render(request, 'pages/login.html')


def sign_up(request):
    return render(request, 'pages/register.html')


@login_required(login_url="login")
def sign_out(request):
    logout(request)
    return redirect(to="home")

@login_required(login_url="login")
def dashboard(request):
    appointments = Appointment.objects.all()
    services = Service.objects.all()
    patients = Group.objects.get(name="patient").user_set.all()
    
    print(patients.count())
    
    
    context = {
        'appointments' : appointments,
        'total_appointment' : appointments.count(),
        'services' : services,
        'total_service' : services.count(),
        'patients' : patients,
        'total_patient' : patients.count() 
    }
    
    return render(request, 'pages/dashboard.html', context)



@login_required(login_url="login")
def service_list(request):
    
    services = Service.objects.all()
    
    context = {
        'services' : services
    }
    
    return render(request, 'pages/services/index.html', context)



@login_required(login_url="login")
def service_create(request):
    
    if request.method == 'POST':
        
        service_data = {
            'image' : request.FILES['image'],
            'name' : request.POST.get('name'),
            'description' : request.POST.get('description'),
            'price' : request.POST.get('price')
        }
        
        
        Service.objects.create(image=service_data['image'], name=service_data['name'], description=service_data['description'], price=service_data['price'])
        
        
        return redirect(to="service_index")
    
    return render(request, 'pages/services/create.html')

@login_required(login_url="login")
def service_show(request, serviceID):
    service = Service.objects.get(id=serviceID)
    
    context = {
        'service' : service
    }
    
    return render(request, 'pages/services/show.html', context)

@login_required(login_url="login")
def service_destroy(request, serviceID):
    service = Service.objects.get(id=serviceID)
    
    service.delete()
    
    return redirect(to="service_index")


@login_required(login_url='login')
def appointment_index(request):
    appointments = Appointment.objects.all()
    context = {
        'appointments' : appointments
    }
    return render(request, 'pages/Appointment/index.html', context)

@login_required(login_url='login')
def appointment_show(request, appointmentID):
    appointment =  Appointment.objects.get(id=appointmentID)
    context = {
        'appointment' : appointment
    }
    return render(request, 'pages/Appointment/show.html', context)


@login_required(login_url="login")
def appointment_edit(request, appointmentID):
    appointment = Appointment.objects.get(id=appointmentID)
    appointmentForm = AppointmentForm(instance=appointment)
    context = {
        'appointment' : appointment,
        'appointmentForm' : appointmentForm
    }
    
    if request.method == 'POST':
        appointmentForm = AppointmentForm(request.POST, instance=appointment)
        appointmentForm.save()
        return redirect(to="appointment_index")
    
    return render(request, 'pages/Appointment/edit.html', context)



@login_required(login_url="login")
def appointment_delete(request, appointmentID):
    appointment = Appointment.objects.get(id=appointmentID)
    appointment.delete()
    return redirect(to="appointment_index")


