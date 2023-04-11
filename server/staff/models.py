from django.db import models
from users.models import BloodGroupEnum, StateEnum
from users.models import Profile

# Create your models here.

class Clinic(models.Model):
    clinic_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()
    state = models.CharField(max_length=20, choices=StateEnum.choices)

class BloodAvailable(models.Model):
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BloodGroupEnum.choices)
    units_available = models.IntegerField()
    models.UniqueConstraint(fields=['clinic_id', 'blood_group'], name='unique_clinic_blood')

class DonorAppointment(models.Model):
    donor_appointment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    datetime_of_appointment = models.DateTimeField()
    appointment_fullfilled = models.BooleanField(default=False) #type: ignore
    models.UniqueConstraint(fields=['user_id', 'clinic_id', 'datetime_of_appointment'], name='unique_user_clinic_datetime')

class PatientAppointment(models.Model):
    patient_appointment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    datetime_of_appointment = models.DateTimeField()
    appointment_fullfilled = models.BooleanField(default=False) #type: ignore
    models.UniqueConstraint(fields=['user_id', 'clinic_id', 'datetime_of_appointment'], name='unique_user_clinic_datetime')

class BloodFromDonor(models.Model):
    blood_id = models.AutoField(primary_key=True)
    appointment_id = models.ForeignKey(DonorAppointment, on_delete=models.CASCADE)
    models.UniqueConstraint(fields=['blood_id', 'appointment_id'], name='unique_appointment')

class BloodToPatient(models.Model):
    blood_id = models.AutoField(primary_key=True)
    appointment_id = models.ForeignKey(PatientAppointment, on_delete=models.CASCADE)
    models.UniqueConstraint(fields=['blood_id', 'appointment_id'], name='unique_appointment')

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    models.UniqueConstraint(fields=['clinic_id', 'user_id'], name='unique_clinic_user')

