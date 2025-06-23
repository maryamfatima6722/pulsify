"""health_desease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from health import views
from health.views import *
# from .api import router
from .apirep import routerep
from health.views import book_appointment_view


from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.utils import timezone
from django.db.models import Count, Sum
from django.http import JsonResponse
import json
from decimal import Decimal
  # Make sure to import your Appointment model


def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

urlpatterns = [
    # path('api/sensoviz/', include(router.urls)),
    path('api/v1/', include(routerep.urls)),
    path('admin/', admin.site.urls),
                  path('reports/', doctor_reports, name='doctor_reports'),

path('add_prescription/<int:appointment_id>/', views.add_prescription, name='add_prescription'),
path('appointment/cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('', Home, name="home"),
path('blog/', include('blog.urls')),
path('contact/', contact_view, name='contact'),
path('simple-page/', views.simple_page, name='simple_page'),
                  path('predict_heart_disease/', predict_heart_disease, name='predict_heart_disease'),
                  path('save_prescription/', views.save_prescription, name='save_prescription'),
                  path('get_prescriptions/', get_prescriptions, name='get_prescriptions'),
path('cancel_appointment/<int:appointment_id>/', CancelAppointmentView.as_view(), name='cancel_appointment'),
 path('view_prescriptions/<int:patient_id>/<int:doctor_id>/', view_prescriptions, name='view_prescriptions'),
path('chatbot/', views.chatbot_view, name='chatbot'),
    path('get_chatbot_response/', views.get_chatbot_response, name='get_chatbot_response'),

                  # Other URL patterns...
    # there is under the patient home i will change User_Home to Patient_Home
    path('patient_home', Patient_Home,name="patient_home"),
    path('doctor_home', Doctor_Home,name="doctor_home"),
    path('admin_home', admin_home,name="admin_home"),
    path('about', About,name="about"),
    path('contact/', views.contact, name='contact'),
    path('gallery', Gallery,name="gallery"),
    path('login', Login_User,name="login"),
    path('login_admin', Login_admin,name="login_admin"),
    path('signup', Signup_User,name="signup"),
    path('logout/', Logout,name="logout"),
    path('change_password', Change_Password,name="change_password"),
    # path('prdict_heart_disease', prdict_heart_disease,name="prdict_heart_disease"),
    path('add_heartdetail', add_heartdetail,name="add_heartdetail"),
    # path('chatbot', chatbot, name="chatbot"),
path('chatbot_view/', views.chatbot_view, name='chatbot_view'),
    path('get_chatbot_response/', views.get_chatbot_response, name='get_chatbot_response'),
    path('information_hub', information_hub, name="information_hub"),

    path('view_search_pat', view_search_pat,name="view_search_pat"),

    path('view_doctor', View_Doctor,name="view_doctor"),
    path('add_doctor', add_doctor,name="add_doctor"),
    path('change_doctor/<int:pid>/', add_doctor,name="change_doctor"),
    path('view_patient', View_Patient,name="view_patient"),
    path('view_feedback', View_Feedback,name="view_feedback"),
    path('edit_profile', Edit_My_deatail,name="edit_profile"),
    path('profile_doctor', View_My_Detail,name="profile_doctor"),
    path('sent_feedback', sent_feedback,name="sent_feedback"),


    #there is following link for logo
# path('carousel', carousel,name="carousel"),
path('appointment/admin_confirm/<int:appointment_id>/', views.admin_confirm_appointment, name='admin_confirm_appointment'),
    path('appointment/admin_cancel/<int:appointment_id>/', views.admin_cancel_appointment, name='admin_cancel_appointment'),



path('error/<str:message>/', error_page, name='error_page'),
    # there is following the link for testing
# path('upload_receipt/', upload_receipt, name='upload_receipt'),
                  path('book_appointment/<int:availability_id>/', views.book_appointment, name='book_appointment'),

# path('book_appointment/<int:availability_id>/', views.book_appointment_view, name='book_appointment'),



                  path('upload_receipt/<int:appointment_id>/', upload_receipt, name='upload_receipt'),
                  path('view_receipt/<int:payment_id>/', view_receipt, name='view_receipt'),

    #for appointment booking links are here
# path('book_appointment/<int:availability_id>/', views.book_appointment, name='book_appointment'),
path('verify_payment/<int:payment_id>/', views.verify_payment, name='verify_payment'),


    #there are following link for add or modify doctor availability
                  path('availabilities/', view_availabilities, name='view_availabilities'),
                  path('add_availability/', add_availability, name='add_availability'),
                  path('edit_availability/<int:availability_id>/', edit_availability, name='edit_availability'),
                  path('delete_availability/<int:availability_id>/', delete_availability, name='delete_availability'),
# Ensure this is in your urls.py
path('verify_payment/<int:appointment_id>/', views.verify_payment, name='verify_payment'),


# path('book_appointment/<int:availability_id>/', views.book_appointment, name='book_appointment'),


path('doctor_availability', doctor_availability,name="doctor_availability"),


    path('delete_searched/<int:pid>', delete_searched, name="delete_searched"),
    path('delete_doctor<int:pid>', delete_doctor, name="delete_doctor"),
    path('assign_status<int:pid>', assign_status, name="assign_status"),
    path('delete_patient<int:pid>', delete_patient, name="delete_patient"),
    path('delete_feedback<int:pid>', delete_feedback, name="delete_feedback"),
    path('predict_desease/<str:pred>/<str:accuracy>/', predict_desease, name="predict_desease"),
    # find doctor
    path('find_doctor/', find_doctor, name='find_doctor'),
# path('doctor_registration/', doctor_registration, name='doctor_registration'),

                  path('appointment/confirm/<int:appointment_id>/', confirm_appointment,name='confirm_appointment'),
                  path('appointment/cancel/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
                  # Other URLs as needed
                  path('manage_appointments/', views.manage_appointments, name='manage_appointments'),
                  # path('appointments/confirm/<int:appointment_id>/', confirm_appointment, name='confirm_appointment'),
                  # path('appointments/cancel/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),

path('doctors/<int:doctor_id>/availability/', views.doctor_availability, name='doctor_availability'),
path('availability/<int:availability_id>/book/', views.book_appointment, name='book_appointment'),
path('patient_appointments/', views.patient_appointments, name='patient_appointments'),

                  path('book_appointment/<int:doctor_id>/<int:availability_id>/', views.book_appointment,
                       name='book_appointment'),

path('appointments/manage/', views.manage_appointments, name='manage_appointments'),
    path('appointment/confirm/<int:appointment_id>/', views.confirm_appointment, name='confirm_appointment'),
    # path('appointment/cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
path('appointment/cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),path('book_appointment/<int:doctor_id>/<int:slot_id>/', book_appointment, name='book_appointment'),
 path('doctor_availability/<int:doctor_id>/', views.doctor_availability, name='doctor_availability'),

path('book_appointment/<int:doctor_id>/', book_appointment_view, name='book_appointment'),
    # Further URLs...

                  path('add_availability/', add_availability, name='add_availability'),
                  path('doctor_availability/<int:doctor_id>/', doctor_availability, name='doctor_availability'),
                  # path('book_appointment/<int:availability_id>/', book_appointment, name='book_appointment'),
 path('availabilities/', view_availabilities, name='view_availabilities'),
    path('DoctorAvailability/', DoctorAvailability, name='DoctorAvailability'),
# path('doctor_availabilities/', all_doctor_availabilities, name='all_doctor_availabilities'),

# path('patient_appointments', views.patient_appointments, name='patient_appointments'),


                  # path('DoctorAvailability/', DoctorAvailability, name='DoctorAvailability'),
                  # path('add_slots/', add_slots, name="add_slots")

    # path('book_appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
