from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Clinic)
admin.site.register(BloodAvailable)
admin.site.register(DonorAppointment)
admin.site.register(PatientAppointment)
admin.site.register(BloodFromDonor)
admin.site.register(BloodToPatient)
admin.site.register(Staff)

