from django.db import models
from users.models import BloodGroupEnum, StateEnum
from users.models import Profile

# Create your models here.

class Clinic(models.Model):
    clinic_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    pincode = models.IntegerField()
    state = models.CharField(max_length=20, choices=StateEnum.choices, null=False, blank=False)

class BloodAvailable(models.Model):
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BloodGroupEnum.choices)
    units_available = models.IntegerField(default = 5)
    models.UniqueConstraint(fields=['clinic_id', 'blood_group'], name='unique_clinic_blood')

# appointment id in both tables should be unique

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=[('Donor', 'Donor'), ('Patient', 'Patient')])
    datetime_of_appointment = models.DateTimeField()
    datetime_of_booking = models.DateTimeField(auto_now_add=True)
    appointment_fullfilled = models.BooleanField(default=False) #type: ignore
    models.UniqueConstraint(fields=['user_id', 'clinic_id', 'datetime_of_appointment'], name='unique_user_clinic_datetime')


class BloodFromDonor(models.Model):
    blood_id = models.AutoField(primary_key=True)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    models.UniqueConstraint(fields=['blood_id', 'appointment_id'], name='unique_appointment')

class BloodToPatient(models.Model):
    blood_id = models.AutoField(primary_key=True)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    models.UniqueConstraint(fields=['blood_id', 'appointment_id'], name='unique_appointment')

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    models.UniqueConstraint(fields=['clinic_id', 'user_id'], name='unique_clinic_user')

