from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


from django import forms
from django.core.exceptions import ValidationError
from .models import Doctor, DoctorAvailability
from django.contrib.auth.models import User

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['contact', 'address', 'category', 'image']  # Update these fields as per your Doctor model
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_time', 'message', 'payment_receipt']
class DoctorAvailabilityForm(forms.ModelForm):
    class Meta:
        model = DoctorAvailability
        fields = ['day', 'start_time', 'end_time', 'fee']  # Include fee in the fields
        widgets = {
            'day': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'fee': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        super().clean()
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("End time must be after start time.")
        return self.cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

# You might also need a form for patients or appointments if you plan to manage them.

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['receipt']  # Ensure this is the correct field for file uploads

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['receipt'].widget.attrs.update({'class': 'form-control'})
    # receipt = forms.FileField(required=True)
class AppointmentBookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_time', 'payment_receipt']  # Include the payment_receipt field

    def __init__(self, *args, **kwargs):
        super(AppointmentBookingForm, self).__init__(*args, **kwargs)
        self.fields['payment_receipt'].required = False  # Make this optional or mandatory based on your requirement


class ChatForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), label='Your Message')

class PredictionForm(forms.Form):
    age = forms.FloatField(label='Age', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your age'
    }))
    gender = forms.ChoiceField(choices=[(1, 'Male'), (0, 'Female')], label='Gender', widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    height = forms.FloatField(label='Height (in cm)', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your height in cm'
    }))
    weight = forms.FloatField(label='Weight (in kg)', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your weight in kg'
    }))
    systolic_bp = forms.FloatField(label='Systolic Blood Pressure', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your systolic blood pressure'
    }))
    diastolic_bp = forms.FloatField(label='Diastolic Blood Pressure', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your diastolic blood pressure'
    }))
    cholesterol = forms.ChoiceField(choices=[(1, 'Normal'), (2, 'Above Normal'), (3, 'Well Above Normal')], label='Cholesterol', widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    glucose = forms.ChoiceField(choices=[(1, 'Normal'), (2, 'Above Normal'), (3, 'Well Above Normal')], label='Glucose', widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    smoking = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Smoking', widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    alcohol_intake = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Alcohol Intake', widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    physical_activity = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Physical Activity', widget=forms.Select(attrs={
        'class': 'form-control'
    }))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['prescription_text']