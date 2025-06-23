

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Doctor(models.Model):
    status = models.IntegerField(null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')

    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    doj = models.DateField(null=True)
    dob = models.DateField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username

class Patient(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username
class DoctorAvailability(models.Model):
    class Weekday(models.TextChoices):
        MONDAY = 'Monday', _('Monday')
        TUESDAY = 'Tuesday', _('Tuesday')
        WEDNESDAY = 'Wednesday', _('Wednesday')
        THURSDAY = 'Thursday', _('Thursday')
        FRIDAY = 'Friday', _('Friday')
        SATURDAY = 'Saturday', _('Saturday')
        SUNDAY = 'Sunday', _('Sunday')

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availabilities')
    day = models.CharField(max_length=9, choices=Weekday.choices, default=Weekday.MONDAY)
    start_time = models.TimeField()
    end_time = models.TimeField()
    fee = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)  # Adding fee field

    def __str__(self):
        return f"{self.doctor.user.username} is available on {self.get_day_display()} from {self.start_time} to {self.end_time}"

    class Meta:
        unique_together = ('doctor', 'day', 'start_time', 'end_time')
        ordering = ['day', 'start_time']

# class Appointment(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     appointment_time = models.DateTimeField()
#     status = models.CharField(max_length=100, choices=(
#         ('pending', 'Pending'),
#         ('confirmed', 'Confirmed'),
#         ('cancelled', 'Cancelled')),
#         default='pending'
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.patient.user.username} appointment with {self.doctor.user.username} on {self.appointment_time}"


class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='payments')
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE, related_name='payments', null=True, blank=True)
    receipt = models.FileField(upload_to='receipts/')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment by {self.patient.user.username} for Appointment {self.appointment.id}"





class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_appointments')
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=100, choices=(
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')),
        default='pending')
    message = models.TextField(null=True, blank=True)
    payment_receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointment_payment')

    def __str__(self):
        return f"{self.patient.user.username} appointment with {self.doctor.user.username} on {self.appointment_time}"




class Admin_Helath_CSV(models.Model):
    name = models.CharField(max_length=100, null=True)
    csv_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

class Search_Data(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    prediction_accuracy = models.CharField(max_length=100, null=True, blank=True)
    result = models.CharField(max_length=100, null=True, blank=True)
    values_list = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.patient.user.username

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    messages = models.TextField(null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username


# class Payment(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='payments')
#     receipt = models.FileField(upload_to='receipts/')
#     verified = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Payment by {self.patient.user.username}"



class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='prescriptions')
    prescription_text = models.TextField()
    date_issued = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.user.username} by Dr. {self.doctor.user.username} on {self.date_issued}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject