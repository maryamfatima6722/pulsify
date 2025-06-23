# import genai
# import genai
import calendar
import decimal
import logging

from _socket import gaierror
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.sites import requests
from django.core.serializers import json
from django.shortcuts import render, redirect
#for sending mail to owner
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
#above are the librarier for sending mail
from django.db.models.functions import TruncMonth

import datetime

from django.utils.decorators import method_decorator
from django.utils.timezone import now
from django.utils.dateparse import parse_datetime
from django.views import View
from django.views.decorators.http import require_POST
from sklearn.ensemble import GradientBoostingClassifier

from .forms import DoctorForm, DoctorAvailabilityForm, AppointmentForm, PaymentForm, PrescriptionForm, ContactForm
from .models import *
from django.contrib.auth import authenticate, login, logout, get_user_model
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
from django.core.exceptions import ValidationError
from smtplib import SMTPException
import socket
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from django.http import HttpResponse
# # Create your views here.
import datetime
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages



from django.utils.dateparse import parse_date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DoctorForm
from .models import *
import datetime
from datetime import date
from .models import DoctorAvailability
import pandas as pd



from django.shortcuts import render
from .models import Doctor  # Import the Doctor model

from django.shortcuts import render, get_object_or_404
from .models import Doctor



from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm



import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
# from generativeai import config, GenerativeModel
from django.shortcuts import render
from django.shortcuts import render
from .forms import ChatForm
import openai
from django.conf import settings
from django.shortcuts import render
import pickle
import os
# Ensure google.generativeai is imported correctly
# health/views.py
from django.shortcuts import render
from django.http import JsonResponse
# health/views.py
from django.shortcuts import render
from django.http import JsonResponse
# health/views.py
from django.shortcuts import render
from django.http import JsonResponse
# health/views.py
from django.shortcuts import render
from django.http import JsonResponse
# health/views.py
from django.shortcuts import render
from django.http import JsonResponse
# health/views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
from .forms import ChatForm
from django.conf import settings
import json  # Ensure you are using the standard Python json module
import openai
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Directly set your OpenAI API key
# api_key = "sk-proj-aZfIiwp1glz4GTTHlSRlT3BlbkFJeFwN7yjKxq6rhq3v3BVN"

import json
import openai
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import cohere
# Initialize Cohere API
cohere_client = cohere.Client(settings.COHERE_API_KEY)

def chatbot_view(request):
    return render(request, "chatbot.html")

@csrf_exempt
def get_chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message")
            if not user_message:
                return JsonResponse({"error": "No message provided."}, status=400)

            response = cohere_client.generate(
                model='command-xlarge-nightly',
                prompt=f"You are a helpful assistant. User: {user_message}",
                max_tokens=500
            )
            bot_message = response.generations[0].text.strip()
            return JsonResponse({"response": bot_message})
        except cohere.CohereError as e:
            return JsonResponse({"error": str(e)}, status=500)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method."}, status=400)



def success(request):
    return render(request, 'doctor_home.html')

def error_page(request, message):
    return render(request, 'error_page.html', {'message': message})



def simple_page(request):
    return render(request, 'simple_page.html')
# Other imports and views definitions above...

def find_doctor(request):
    doctors = Doctor.objects.all()  # Retrieve all available doctors
    return render(request, 'find_doctor.html', {'doctors': doctors})






def doctor_availability(request):
    today = timezone.localdate()  # Ensure it captures the current date appropriately.
    availabilities = DoctorAvailability.objects.filter(day__gte=today).select_related('doctor').order_by('doctor', 'day', 'start_time')
    return render(request, 'all_doctor_availabilities.html', {'availabilities': availabilities})


from datetime import datetime, timedelta


def next_weekday(d, weekday):
    """
    d: Current date
    weekday: The desired weekday as an integer, where Monday is 0 and Sunday is 6.
    """
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)


from django.utils import timezone

import datetime  # This imports the datetime module


import datetime
User = get_user_model()

from django.utils import timezone
from datetime import datetime, date  # Correctly import datetime and date
import datetime
from datetime import datetime, date, time


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)







@login_required
def book_appointment(request, availability_id):
    availability = get_object_or_404(DoctorAvailability, pk=availability_id)
    today = datetime.today().date()
    weekday_dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    if request.method == 'POST':
        try:
            patient = request.user.patient
        except AttributeError:
            messages.error(request, "No patient profile associated with this user.")
            return redirect('error_page')

        # Get the next date for the given weekday
        next_date = today + timedelta((weekday_dict[availability.day] - today.weekday() + 7) % 7)
        appointment_datetime = datetime.combine(next_date, availability.start_time)

        # Check for existing appointments on the same day for the same doctor
        existing_appointments = Appointment.objects.filter(
            doctor=availability.doctor,
            appointment_time__date=next_date
        ).order_by('appointment_time')

        if existing_appointments.exists():
            last_appointment = existing_appointments.last()
            appointment_datetime = last_appointment.appointment_time + timedelta(minutes=20)

        # Create the appointment
        try:
            appointment = Appointment.objects.create(
                patient=patient,
                doctor=availability.doctor,
                appointment_time=appointment_datetime,
                status='pending'
            )

            # Send email to admin
            # send_mail(
            #     'New Appointment Request',
            #     f'New appointment request from {patient.user.username} for Dr. {availability.doctor.user.username} on {appointment_datetime}.',
            #     settings.DEFAULT_FROM_EMAIL,
            #     [settings.DEFAULT_FROM_EMAIL],  # Admin email address
            #     fail_silently=False,
            # )

            messages.success(request, "Appointment booked successfully.")
            return redirect('upload_receipt', appointment_id=appointment.id)
        except Exception as e:
            messages.error(request, f"Failed to book appointment: {str(e)}")
            return render(request, 'book_appointment.html', {'availability': availability})

    return render(request, 'book_appointment.html', {'availability': availability})






@login_required
def upload_receipt(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    patient = appointment.patient  # Get the patient from the appointment

    if request.method == 'POST':
        receipt_file = request.FILES.get('receipt')
        if receipt_file:
            try:
                # Create a Payment record and associate it with the patient and receipt
                payment = Payment(patient=patient, receipt=receipt_file)
                payment.save()

                # Link the payment to the appointment
                appointment.payment = payment
                appointment.save()

                messages.success(request, "Receipt uploaded successfully.")
                return redirect('patient_appointments')  # Redirect to a success or listing page
            except Exception as e:
                messages.error(request, f"Failed to upload receipt: {str(e)}")
        else:
            messages.error(request, "No file was uploaded.")

    return render(request, 'upload_receipt.html', {'appointment_id': appointment_id})



@login_required
@user_passes_test(lambda u: u.is_staff)
def verify_payment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    if request.method == 'POST':
        if 'verify' in request.POST:
            payment.verified = True
            payment.appointment.status = 'confirmed'
            messages.success(request, "Payment verified, appointment confirmed.")
        elif 'reject' in request.POST:
            payment.appointment.status = 'cancelled'
            messages.info(request, "Payment rejected, appointment cancelled.")
        payment.save()
        payment.appointment.save()
        return redirect('admin_appointment_management')
    return render(request, 'admin_verify_payment.html', {'payment': payment})




@login_required
def admin_confirm_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        appointment.status = 'confirmed'
        appointment.save()

        try:
            # Send email to patient and doctor
            send_mail(
                'Appointment Confirmed',
                f'Your appointment with Dr. {appointment.doctor.user.username} on {appointment.appointment_time} has been confirmed.',
                settings.DEFAULT_FROM_EMAIL,
                [appointment.patient.user.email, appointment.doctor.user.email],
                fail_silently=False,
            )
            messages.success(request, 'Appointment confirmed successfully and notification email sent.')
        except (SMTPException, socket.timeout, gaierror) as e:
            # Handle email sending errors
            messages.error(request, f'Appointment confirmed, but failed to send email notification: {str(e)}')

        return redirect('admin_home')  # Redirect to the admin dashboard or any appropriate page

    return render(request, 'admin_confirm_appointment.html', {'appointment': appointment})

@login_required
def admin_cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        appointment.status = 'cancelled'
        appointment.save()

        try:
            # Send email to patient and doctor
            send_mail(
                'Appointment Cancelled',
                f'Your appointment with Dr. {appointment.doctor.user.username} on {appointment.appointment_time} has been cancelled.',
                settings.DEFAULT_FROM_EMAIL,
                [appointment.patient.user.email, appointment.doctor.user.email],
                fail_silently=False,
            )
            messages.success(request, 'Appointment cancelled and notification email sent.')
        except (SMTPException, socket.timeout, gaierror) as e:
            # Handle email sending errors
            messages.error(request, f'Appointment cancelled, but failed to send email notification: {str(e)}')

        return redirect('admin_home')  # Redirect to the admin dashboard or any appropriate page

    return render(request, 'admin_cancel_appointment.html', {'appointment': appointment})
@login_required(login_url='login')

def book_appointment_view(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.patient = request.user.patient
            appointment.status = 'awaiting_confirmation'
            appointment.save()
            messages.success(request, "Appointment booked successfully, pending payment verification.")
            return redirect('patient_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form, 'doctor': doctor})

@login_required(login_url='login')
def patient_appointments(request):
    if hasattr(request.user, 'patient'):
        patient = request.user.patient
        now = timezone.now()
        appointments = Appointment.objects.filter(patient=patient, appointment_time__gte=now).order_by('appointment_time')
        return render(request, 'patient_appointments.html', {'appointments': appointments})
    else:
        messages.error(request, "You do not have permission to view this page or are not registered as a patient.")
        return redirect('patient_home')


# doctor to add his availabiluty view

# Add Availability
@login_required
def add_availability(request):
    if request.method == 'POST':
        form = DoctorAvailabilityForm(request.POST)
        if form.is_valid():
            new_availability = form.save(commit=False)
            new_availability.doctor = request.user.doctor_profile
            new_availability.save()
            messages.success(request, 'Availability added successfully.')
            return redirect('view_availabilities')
    else:
        form = DoctorAvailabilityForm()

    return render(request, 'add_availability.html', {'form': form})

# Edit Availability
@login_required
def edit_availability(request, availability_id):
    availability = get_object_or_404(DoctorAvailability, id=availability_id, doctor=request.user.doctor_profile)
    if request.method == 'POST':
        form = DoctorAvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            form.save()
            messages.success(request, 'Availability updated successfully.')
            return redirect('view_availabilities')
    else:
        form = DoctorAvailabilityForm(instance=availability)

    return render(request, 'add_availability.html', {'form': form})


@login_required
def delete_availability(request, availability_id):
    availability = get_object_or_404(DoctorAvailability, id=availability_id, doctor=request.user.doctor_profile)

    if request.method == 'POST':  # Ensure this action is confirmed via POST
        availability.delete()
        messages.success(request, "Availability has been successfully deleted.")
        return redirect('view_availabilities')
    else:
        # Optionally, you could also handle GET request differently or confirm before deletion
        return render(request, 'confirm_delete.html', {'availability': availability})


@login_required(login_url="login")
def view_availabilities(request):
    try:
        # Assuming the doctor profile is directly linked with the user model
        if hasattr(request.user, 'doctor_profile'):
            availabilities = DoctorAvailability.objects.filter(
                # print(request.user.doctor_profile)
                doctor=request.user.doctor_profile
            ).order_by('day', 'start_time')

            if not availabilities.exists():
                messages.info(request, "You have no availabilities set up yet.")
            return render(request, 'view_availabilities.html', {
                'availabilities': availabilities
            })
        else:
            messages.error(request, "You are not authorized to view this page or need a doctor profile set up.")
            return redirect('home')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('home')
# Other views definitions continue below...




# for call and chat



def Home(request):
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()

    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
    }

    return render(request, 'carousel.html', context)

def contact(request):

    return render(request, 'contact.html')



@login_required
def admin_home(request):
    try:
        # Counts for various entities

        dis_count = Search_Data.objects.count()
        pat_count = Patient.objects.count()
        doc_count = Doctor.objects.count()
        feed_count = Feedback.objects.count()
        contact_msgs = Contact.objects.all()
        contact_msgs_count = contact_msgs.count()

        # Fetch all appointments with their related data to reduce database hits
        appointments = Appointment.objects.all().select_related('doctor', 'patient', 'payment')

        context = {
            'dis_count': dis_count,
            'pat_count': pat_count,
            'doc_count': doc_count,
            'feed_count': feed_count,
            'appointments': appointments,
            'contact_msgs': contact_msgs,
            'contact_msgs_count': contact_msgs_count,
        }
        return render(request, 'admin_home.html', context)

    except Exception as e:
        messages.error(request, "Error loading data for admin dashboard.")
        return render(request, 'admin_home.html', {'error': 'Error loading data.'})


def view_receipt(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    context = {
        'payment': payment
    }
    return render(request, 'view_receipt.html', context)



@login_required(login_url="login")
def assign_status(request, pid):
    doctor = Doctor.objects.get(id=pid)
    if doctor.status == 1:
        doctor.status = 2
        messages.success(request, 'Selected doctor has successfully withdrawn approval.')
    else:
        doctor.status = 1
        messages.success(request, 'Selected doctor has successfully approved.')
    doctor.save()
    return redirect('view_doctor')

@login_required(login_url="login")
def Patient_Home(request):
    patient = request.user.patient  # Assuming the logged-in user is a patient
    prescriptions = Prescription.objects.filter(patient=patient).order_by('-date_issued')

    context = {
        'prescriptions': prescriptions
    }
    return render(request, 'patient_home.html', context)

# @login_required(login_url="login")
# def Doctor_Home(request):
#     return render(request, 'doctor_home.html')

@login_required(login_url='login')
def Doctor_Home(request):
    if hasattr(request.user, 'doctor_profile'):
        doctor = request.user.doctor_profile
        now = timezone.now()
        appointments = Appointment.objects.filter(doctor=doctor, appointment_time__gte=now).order_by('appointment_time')
        return render(request, 'doctor_home.html', {'appointments': appointments})
    else:
        messages.error(request, "You're not authorized to view this page.")
        return redirect('home')



@method_decorator(csrf_exempt, name='dispatch')
class CancelAppointmentView(View):
    def post(self, request, appointment_id):
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            if appointment.status == 'pending':
                appointment.status = 'cancelled'
                appointment.save()
                return JsonResponse({'message': 'Appointment cancelled successfully.'}, status=200)
            else:
                return JsonResponse({'message': 'Cannot cancel a confirmed appointment.'}, status=400)
        except Appointment.DoesNotExist:
            return JsonResponse({'message': 'Appointment not found.'}, status=404)

@login_required
def manage_appointments(request):
    if hasattr(request.user, 'doctor_profile'):
        appointments = request.user.doctor_profile.appointments.filter(status='pending')
        return render(request, 'manage_appointments.html', {'appointments': appointments})
    else:
        messages.error(request, "You're not authorized to view this page.")
        return redirect('home')

@login_required
def confirm_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id, doctor=request.user.doctor_profile)
    if request.method == 'POST':
        appointment.status = 'confirmed'
        appointment.save()
        messages.success(request, 'Appointment confirmed.')
        return redirect('manage_appointments')
    return render(request, 'confirm_appointment.html', {'appointment': appointment})
@require_POST
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = 'cancelled'
    appointment.save()
    return JsonResponse({'success': True})
@login_required
def cancel_appointment(request, appointment_id):
    # Ensure the appointment belongs to the logged-in user
    appointment = get_object_or_404(Appointment, pk=appointment_id, patient=request.user)
    if request.method == 'POST':
        appointment.status = 'cancelled'
        appointment.save()
        messages.success(request, 'Appointment cancelled.')
        return redirect('manage_appointments')
    return render(request, 'cancel_appointment.html', {'appointment': appointment})


@login_required
@user_passes_test(lambda u: u.is_superuser)  # Ensure only admins can access this view
def verify_payment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        if 'verify' in request.POST:
            appointment.payment_verified = True
            appointment.status = 'confirmed'
            messages.success(request, "Payment verified, appointment confirmed.")
        elif 'deny' in request.POST:
            appointment.status = 'cancelled'
            messages.info(request, "Payment denied, appointment cancelled.")
        appointment.save()
        return redirect('admin_appointment_management')
    return render(request, 'admin/verify_payment.html', {'appointment': appointment})



def About(request):
    return render(request, 'about.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def information_hub(request):
    return render(request, 'information_hub.html')

def Gallery(request):
    return render(request, 'gallery.html')

def Login_User(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        sign = ""
        if user:
            try:
                sign = Patient.objects.get(user=user)
            except:
                pass
            if sign:
                login(request, user)
                error = "pat1"
            else:
                pure = False
                try:
                    pure = Doctor.objects.get(status=1, user=user)
                except:
                    pass
                if pure:
                    login(request, user)
                    error = "pat2"
                else:
                    login(request, user)
                    error = "notmember"
        else:
            error = "not"
    d = {'error': error}
    return render(request, 'login.html', d)

def Login_admin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user.is_staff:
            login(request, user)
            error = "pat"
        else:
            error = "not"
    d = {'error': error}
    return render(request, 'admin_login.html', d)

# def Signup_User(request):
#     error = ""
#     if request.method == 'POST':
#         f = request.POST['fname']
#         l = request.POST['lname']
#         u = request.POST['uname']
#         e = request.POST['email']
#         p = request.POST['pwd']
#         d = request.POST['dob']
#         con = request.POST['contact']
#         add = request.POST['add']
#         type = request.POST['type']
#         im = request.FILES['image']
#         dat = datetime.date.today()
#         user = User.objects.create_user(email=e, username=u, password=p, first_name=f,last_name=l)
#         if type == "Patient":
#             Patient.objects.create(user=user,contact=con,address=add,image=im,dob=d)
#         else:
#             Doctor.objects.create(dob=d,image=im,user=user,contact=con,address=add,status=2)
#         error = "create"
#     d = {'error':error}
#     return render(request, 'register.html', d)
from datetime import date  # Ensure this import is present

def Signup_User(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        p = request.POST['pwd']
        d = request.POST['dob']
        con = request.POST['contact']
        add = request.POST['add']
        type = request.POST['type']
        im = request.FILES['image']
        dat = date.today()  # Correct usage of date.today()

        user = User.objects.create_user(email=e, username=u, password=p, first_name=f, last_name=l)
        if type == "Patient":
            Patient.objects.create(user=user, contact=con, address=add, image=im, dob=d)
        else:
            Doctor.objects.create(dob=d, image=im, user=user, contact=con, address=add, status=2)
        error = "create"
    d = {'error': error}
    return render(request, 'register.html', d)


def Logout(request):
    logout(request)
    return redirect('home')


# for booking appointment system
@login_required(login_url='login')
def confirm_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor__user=request.user)
    appointment.status = 'confirmed'
    appointment.save()
    messages.success(request, 'Appointment confirmed successfully.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='login')
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor__user=request.user)
    appointment.status = 'cancelled'
    appointment.save()
    messages.error(request, 'Appointment cancelled.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))





@login_required(login_url="login")
def Change_Password(request):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    if not request.user.is_staff:
        try:
            sign = Patient.objects.get(user=user)
            if sign:
                error = "pat"
        except:
            sign = Doctor.objects.get(user=user)
    terror = ""
    if request.method == "POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            terror = "yes"
        else:
            terror = "not"
    d = {'error':error,'terror':terror,'data':sign}
    return render(request,'change_password.html',d)

def preprocess_inputs(df, scaler):
    df = df.copy()
    y = df['target'].copy()
    X = df.drop('target', axis=1).copy()
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    return X, y






def prdict_heart_disease(list_data):
    csv_file = Admin_Helath_CSV.objects.get(id=1)
    df = pd.read_csv(csv_file.csv_file)

    X = df[['age','sex','cp',  'trestbps',  'chol',  'fbs',  'restecg',  'thalach',  'exang',  'oldpeak',  'slope',  'ca',  'thal']]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)
    nn_model = GradientBoostingClassifier(n_estimators=100,learning_rate=1.0,max_depth=1, random_state=0)
    nn_model.fit(X_train, y_train)
    pred = nn_model.predict([list_data])
    print("Neural Network Accuracy: {:.2f}%".format(nn_model.score(X_test, y_test) * 100))
    print("Prdicted Value is : ", format(pred))
    dataframe = str(df.head())
    return (nn_model.score(X_test, y_test) * 100),(pred)

@login_required(login_url="login")
def add_doctor(request,pid=None):
    doctor = None
    if pid:
        doctor = Doctor.objects.get(id=pid)
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES, instance = doctor)
        if form.is_valid():
            new_doc = form.save()
            new_doc.status = 1
            if not pid:
                user = User.objects.create_user(password=request.POST['password'], username=request.POST['username'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                new_doc.user = user
            new_doc.save()
            return redirect('view_doctor')
    d = {"doctor": doctor}
    return render(request, 'add_doctor.html', d)

@login_required(login_url="login")
def add_heartdetail(request):
    if request.method == "POST":
        # list_data = [57, 0, 1, 130, 236, 0, 0, 174, 0, 0.0, 1, 1, 2]
        list_data = []
        value_dict = eval(str(request.POST)[12:-1])
        count = 0
        for key,value in value_dict.items():
            if count == 0:
                count =1
                continue
            if key == "sex" and value[0] == "Male" or value[0] == 'male' or value[0]=='m' or value[0] == 'M':
                list_data.append(0)
                continue
            elif key == "sex":
                list_data.append(1)
                continue
            list_data.append(value[0])

        # list_data = [57, 0, 1, 130, 236, 0, 0, 174, 0, 0.0, 1, 1, 2]
        accuracy,pred = prdict_heart_disease(list_data)
        patient = Patient.objects.get(user=request.user)
        Search_Data.objects.create(patient=patient, prediction_accuracy=accuracy, result=pred[0], values_list=list_data)
        rem = int(pred[0])
        print("Result = ",rem)
        if pred[0] == 0:
            pred = "<span style='color:green'>You are healthy</span>"
        else:
            pred = "<span style='color:red'>You are Unhealthy, Need to Checkup.</span>"
        return redirect('predict_desease', str(rem), str(accuracy))
    return render(request, 'add_heartdetail.html')

@login_required(login_url="login")
def predict_desease(request, pred, accuracy):
    doctor = Doctor.objects.filter(address__icontains=Patient.objects.get(user=request.user).address)
    d = {'pred': pred, 'accuracy':accuracy, 'doctor':doctor}
    return render(request, 'predict_disease.html', d)

@login_required(login_url="login")
def view_search_pat(request):
    doc = None
    data = None
    try:
        doc = Doctor.objects.get(user=request.user)
        data = Search_Data.objects.filter(patient__address__icontains=doc.address).order_by('-id')
    except Doctor.DoesNotExist:
        try:
            doc = Patient.objects.get(user=request.user)
            data = Search_Data.objects.filter(patient=doc).order_by('-id')
        except Patient.DoesNotExist:
            data = Search_Data.objects.all().order_by('-id')

    # Prepare data for the monthly searches chart
    current_year = now().year
    monthly_searches = Search_Data.objects.filter(created__year=current_year).annotate(
        month=TruncMonth('created')
    ).values('month').annotate(search_count=Count('id')).order_by('month')

    # Format data for Chart.js
    months = [calendar.month_name[i] for i in range(1, 13)]
    search_counts = [0] * 12
    for item in monthly_searches:
        month_index = item['month'].month - 1
        search_counts[month_index] = item['search_count']

    context = {
        'data': data,
        'months': months,
        'search_counts': search_counts,
    }
    return render(request, 'view_search_pat.html', context)


@login_required(login_url="login")
def delete_doctor(request,pid):
    doc = Doctor.objects.get(id=pid)
    doc.delete()
    return redirect('view_doctor')

@login_required(login_url="login")
def delete_feedback(request,pid):
    doc = Feedback.objects.get(id=pid)
    doc.delete()
    return redirect('view_feedback')

@login_required(login_url="login")
def delete_patient(request,pid):
    doc = Patient.objects.get(id=pid)
    doc.delete()
    return redirect('view_patient')

@login_required(login_url="login")
def delete_searched(request,pid):
    doc = Search_Data.objects.get(id=pid)
    doc.delete()
    return redirect('view_search_pat')

@login_required(login_url="login")
def View_Doctor(request):
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)

@login_required(login_url="login")
def View_Patient(request):
    patient = Patient.objects.all()
    d = {'patient':patient}
    return render(request,'view_patient.html',d)

@login_required(login_url="login")
def View_Feedback(request):
    dis = Feedback.objects.all()
    d = {'dis':dis}
    return render(request,'view_feedback.html',d)

@login_required(login_url="login")
def View_My_Detail(request):
    terror = ""
    user = User.objects.get(id=request.user.id)
    error = ""
    try:
        sign = Patient.objects.get(user=user)
        error = "pat"
    except:
        sign = Doctor.objects.get(user=user)
    d = {'error': error,'pro':sign}
    return render(request,'profile_doctor.html',d)

@login_required(login_url="login")
def Edit_Doctor(request,pid):
    doc = Doctor.objects.get(id=pid)
    error = ""
    # type = Type.objects.all()
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        add = request.POST['add']
        cat = request.POST['type']
        try:
            im = request.FILES['image']
            doc.image=im
            doc.save()
        except:
            pass
        dat = datetime.date.today()
        doc.user.first_name = f
        doc.user.last_name = l
        doc.user.email = e
        doc.contact = con
        doc.category = cat
        doc.address = add
        doc.user.save()
        doc.save()
        error = "create"
    d = {'error':error,'doc':doc,'type':type}
    return render(request,'edit_doctor.html',d)
from datetime import date  # Ensure this import is at the top of your file

@login_required(login_url="login")
def Edit_My_deatail(request):
    terror = ""
    user = User.objects.get(id=request.user.id)
    error = ""
    try:
        sign = Patient.objects.get(user=user)
        error = "pat"
    except:
        sign = Doctor.objects.get(user=user)

    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        add = request.POST['add']
        try:
            im = request.FILES['image']
            sign.image = im
            sign.save()
        except:
            pass
        to1 = date.today()  # Correct usage of date.today()
        sign.user.first_name = f
        sign.user.last_name = l
        sign.user.email = e
        sign.contact = con
        if error != "pat":
            cat = request.POST['type']
            sign.category = cat
            sign.save()
        sign.address = add
        sign.user.save()
        sign.save()
        terror = "create"
    d = {'error': error, 'terror': terror, 'doc': sign}
    return render(request, 'edit_profile.html', d)


@login_required(login_url='login')
def sent_feedback(request):
    terror = None
    if request.method == "POST":
        username = request.POST['uname']
        message = request.POST['msg']
        username = User.objects.get(username=username)
        Feedback.objects.create(user=username, messages=message)
        terror = "create"
    return render(request, 'sent_feedback.html',{'terror':terror})






from django.shortcuts import render
from django.conf import settings
import os
import pandas as pd
import numpy as np
from .forms import PredictionForm
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier

# Load and preprocess the dataset once
data_path = os.path.join(settings.BASE_DIR, 'data', 'cardio_train.csv')
data = pd.read_csv(data_path, sep=';')
imputer = SimpleImputer(strategy='mean')
data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
X = data_imputed.drop(['id', 'cardio'], axis=1)
y = data_imputed['cardio']
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
model_gb = GradientBoostingClassifier(random_state=42)
model_gb.fit(X_scaled, y)

def predict_heart_disease(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Extract data from form
            input_data = [
                form.cleaned_data['age'],
                form.cleaned_data['gender'],
                form.cleaned_data['height'],
                form.cleaned_data['weight'],
                form.cleaned_data['systolic_bp'],
                form.cleaned_data['diastolic_bp'],
                form.cleaned_data['cholesterol'],
                form.cleaned_data['glucose'],
                form.cleaned_data['smoking'],
                form.cleaned_data['alcohol_intake'],
                form.cleaned_data['physical_activity']
            ]
            input_data = np.array(input_data, dtype=float).reshape(1, -1)
            input_data_scaled = scaler.transform(input_data)
            prediction = model_gb.predict(input_data_scaled)
            result = 'Positive' if prediction[0] == 1 else 'Negative'
            return render(request, 'predict_heart_disease.html', {'form': form, 'result': result})
    else:
        form = PredictionForm()
    return render(request, 'predict_heart_disease.html', {'form': form})


from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count, Sum, F
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError



from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.utils import timezone
from django.db.models import Count, Sum
from django.http import JsonResponse
import json
from decimal import Decimal
from .models import Appointment  # Make sure to import your Appointment model



@login_required
@staff_member_required
def doctor_reports(request):
    try:
        now = timezone.now()

        daily_reports = list(Appointment.objects.filter(
            appointment_time__date=now.date()
        ).values('doctor__user__username').annotate(
            count=Count('id'),
            revenue=Sum('doctor__availabilities__fee')
        ).order_by('-count'))

        weekly_reports = list(Appointment.objects.filter(
            appointment_time__week=now.isocalendar()[1], 
            appointment_time__year=now.year
        ).values('doctor__user__username').annotate(
            count=Count('id'),
            revenue=Sum('doctor__availabilities__fee')
        ).order_by('-count'))

        monthly_reports = list(Appointment.objects.filter(
            appointment_time__month=now.month, 
            appointment_time__year=now.year
        ).values('doctor__user__username').annotate(
            count=Count('id'),
            revenue=Sum('doctor__availabilities__fee')
        ).order_by('-count'))

        yearly_reports = list(Appointment.objects.filter(
            appointment_time__year=now.year
        ).values('doctor__user__username').annotate(
            count=Count('id'),
            revenue=Sum('doctor__availabilities__fee')
        ).order_by('-count'))

        context = {
            'daily_reports': daily_reports,
            'weekly_reports': weekly_reports,
            'monthly_reports': monthly_reports,
            'yearly_reports': yearly_reports,
            'daily_reports_json': json.dumps(daily_reports, default=decimal_default),
            'weekly_reports_json': json.dumps(weekly_reports, default=decimal_default),
            'monthly_reports_json': json.dumps(monthly_reports, default=decimal_default),
            'yearly_reports_json': json.dumps(yearly_reports, default=decimal_default)
        }

        return render(request, 'doctor_reports.html', context)

    except Exception as e:
        # Log the error for debugging
        print(f"Error generating reports: {str(e)}")
        # Return a simple error message or redirect
        return render(request, 'error.html', {'message': 'Error generating reports'})


@login_required
def add_prescription(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = appointment.doctor
            prescription.patient = appointment.patient
            prescription.appointment = appointment
            prescription.save()
            return redirect('doctor_dashboard')
    else:
        form = PrescriptionForm()
    return render(request, 'add_prescription.html', {'form': form, 'appointment': appointment})


@require_POST
def save_prescription(request):
    appointment_id = request.POST.get('appointment_id')
    prescription_text = request.POST.get('description')

    # Fetch the appointment, doctor, and patient associated with this prescription
    appointment = get_object_or_404(Appointment, id=appointment_id)
    patient = appointment.patient
    doctor = appointment.doctor

    # Create and save the prescription
    Prescription.objects.create(
        doctor=doctor,
        patient=patient,
        appointment=appointment,
        prescription_text=prescription_text
    )

    # Redirect to a success page or back to the appointment page
    return redirect(
        'doctor_home')  # Replace 'some_view_name' with the actual name of the view you want to redirect to


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Prescription

@login_required
def get_prescriptions(request):
    if request.method == 'GET':
        doctor_id = request.GET.get('doctor_id')
        patient_id = request.GET.get('patient_id')
        prescriptions = Prescription.objects.filter(doctor_id=doctor_id, patient_id=patient_id).values('prescription_text', 'date_issued')
        prescriptions_list = list(prescriptions)
        return JsonResponse({'prescriptions': prescriptions_list})

@login_required
def view_prescriptions(request, patient_id, doctor_id):
    patient = get_object_or_404(Patient, id=patient_id)
    doctor = get_object_or_404(Doctor, id=doctor_id)
    prescriptions = Prescription.objects.filter(doctor=doctor, patient=patient)

    context = {
        'patient': patient,
        'doctor': doctor,
        'prescriptions': prescriptions,
    }
    return render(request, 'view_prescriptions.html', context)





def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'carousel.html', {'form': form})

# there is the following view for testinng the payment table
