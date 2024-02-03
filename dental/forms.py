from django import forms
from .models import *

class AppointmentForm(forms.ModelForm):
    class Meta :
        model = Appointment
        fields  = '__all__'
        widgets = {
            'date' : forms.DateInput(attrs={'class' : 'input input-accent bg-gray-100'}),
            'patient' : forms.TextInput(attrs={'class' : 'input input-accent bg-gray-100'}),
            'service' : forms.Select(attrs={'class': 'select select-accent bg-gray-100'})
        }