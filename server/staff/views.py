from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from users.models import Profile

# Create your views here.

def staff_homepage(request):
    if not request.user.is_authenticated:
        return redirect('user-login')
    if not request.user.is_staff:
        return render(request, 'not_allowed.html')
    context = {}
    return render(request, 'staff/homepage.html', context)


class Appointment:
    def __init__(self, name, datetime, phone, email, type, fullfilled):
        self.name = name
        self.datetime = datetime
        self.phone = phone
        self.email = email
        self.type = type
        self.fullfilled = fullfilled


def view_appointments(request):
    if not request.user.is_authenticated:
        return redirect('user-login')
    if not request.user.is_staff:
        return render(request, 'not_allowed.html')

    query_name = request.GET.get('name', '')
    staff = Staff.objects.get(user_id=request.user)

    appointments = []
    if query_name == '':
        donor_appointments = DonorAppointment.objects.all().filter(clinic_id=staff.clinic_id).order_by('datetime_of_appointment')
        patient_appointments = PatientAppointment.objects.all().filter(clinic_id=staff.clinic_id).order_by('datetime_of_appointment')
        for appointment in donor_appointments:
            appointments.append(Appointment(
                appointment.user_id.name,
                appointment.datetime_of_appointment,
                appointment.user_id.phone,
                appointment.user_id.email,
                'Donor',
                appointment.appointment_fullfilled
            ))
        for appointment in patient_appointments:
            appointments.append(Appointment(
                appointment.user_id.name,
                appointment.datetime_of_appointment,
                appointment.user_id.phone,
                appointment.user_id.email,
                'Patient',
                appointment.appointment_fullfilled
            ))


    context = {'appointments': appointments}
    return render(request, 'staff/view-appointments.html', context)


def fullfill_appointment(request, appointment_id):
    if not request.user.is_authenticated:
        return redirect('user-login')
    if not request.user.is_staff:
        return render(request, 'not-allowed.html')

    staff = Staff.objects.get(user_id=request.user)

    if DonorAppointment.objects.filter(appointment_id=appointment_id).exists():
        donor_appointment = DonorAppointment.objects.get(appointment_id=appointment_id)
        context = {'appointment': donor_appointment}
        if donor_appointment.appointment_fullfilled:
            return render(request, 'staff/already-fullfilled.html')
        if request.method == 'POST':
            form = BloodUnitsForm(request.POST)
            if form.is_valid():
                blood_units = form.cleaned_data['blood_units']
                bloods = []
                for i in range(blood_units):
                    blood = BloodFromDonor(appointment_id = donor_appointment)
                    try:
                        blood.full_clean()
                    except ValidationError as e:
                        return render(request, 'staff/fullfill-donor-appointment.html', {'errors': e})
                    bloods.append(blood)
                BloodFromDonor.objects.bulk_create(bloods)
                donor_appointment.appointment_fullfilled = True
                donor_appointment.save()
                return render(request, 'staff/already-fullfilled.html', context)
            else:
                return render(request, 'staff/fullfill-donor-appointment.html', {'errors': form.errors})
        else:
            form = BloodUnitsForm()
            context['form'] = form
            return render(request, 'staff/fullfill-donor-appointment.html', context)

    if PatientAppointment.objects.filter(appointment_id=appointment_id).exists():
        patient_appointment = PatientAppointment.objects.get(appointment_id=appointment_id)
        context = {'appointment': patient_appointment}
        if patient_appointment.appointment_fullfilled:
            return render(request, 'staff/already-fullfilled.html')
        if request.method == 'POST':
            form = BloodUnitsForm(request.POST)
            if form.is_valid():
                blood_units = form.cleaned_data['blood_units']
                bloods = []
                for i in range(blood_units):
                    blood = BloodToPatient(appointment_id = patient_appointment)
                    try:
                        blood.full_clean()
                    except ValidationError as e:
                        return render(request, 'staff/fullfill-patient-appointment.html', {'errors': e})
                    bloods.append(blood)
                BloodToPatient.objects.bulk_create(bloods)
                patient_appointment.appointment_fullfilled = True
                patient_appointment.save()
                return render(request, 'staff/already-fullfilled.html', context)
            else:
                return render(request, 'staff/fullfill-donor-appointment.html', {'errors': form.errors})
        else:
            form = BloodUnitsForm()
            context['form'] = form
            return render(request, 'staff/fullfill-donor-appointment.html', context)

    return render(request, 'does-not-exist.html')

