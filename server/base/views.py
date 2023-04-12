from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from staff.models import DonorAppointment, PatientAppointment, Clinic
from .forms import CreateAppointmentForm

TEMPLATE_HOMEPAGE = "homepage.html"
TEMPLATE_EVENTS = "events.html"
TEMPLATE_ABOUT_US = "about-us.html"
TEMPLATE_DONATE_BLOOD = "donate-blood.html"
TEMPLATE_REQUEST_BLOOD = "request-blood.html"
TEMPLATE_DONATIONS = "donations.html"
TEMPLATE_VOLUNTEER = "volunteer.html"

# Create your views here.
def homepage(request):
    context = {}
    return render(request, TEMPLATE_HOMEPAGE, context)

def events(request):
    context = {}
    return render(request, TEMPLATE_EVENTS, context)

def about_us(request):
    context = {}
    return render(request, TEMPLATE_ABOUT_US, context)


def create_appointment(request):
    if not request.user.is_authenticated:
        return redirect('user-login')

    # find if already an appointment
    context = {}

    if DonorAppointment.objects.filter(user_id=request.user).exists() or PatientAppointment.objects.filter(user_id=request.user).exists():
        return render(request, 'base/already-appointment.html', context)

    if request.method == 'POST':
        form = CreateAppointmentForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            clinic_id = form.cleaned_data['clinic']
            clinic = Clinic.objects.get(clinic_id=clinic_id)
            if type == 'Donor':
                appointment = DonorAppointment(
                    user_id=request.user,
                    clinic_id=clinic,
                    datetime_of_appointment=form.cleaned_data['datetime']
                )
            elif type == 'Patient':
                appointment = PatientAppointment(
                    user_id=request.user,
                    clinic_id=clinic,
                    datetime_of_appointment=form.cleaned_data['datetime']
                )
            else:
                messages.error(request, 'Invalid appointment type')
                return redirect('user-create-appointment')

            try:
                appointment.full_clean()
            except ValidationError as e:
                messages.error(request, "There was an error creating the appointment.")
                messages.error(request, e)
            else:
                appointment.save()
                messages.success(request, 'Appointment created successfully')
                return redirect('user-view-appointments')
    else:
        form = CreateAppointmentForm()
    context = {'form': form}
    return render(request, 'base/create-appointment.html', context)

class Appointment:
    def __init__(self, type: str, clinic_name, datetime_of_appointment, datetime_of_booking, fullfilled):
        self.type = type
        self.clinic_name = clinic_name
        self.datetime_of_appointment = datetime_of_appointment
        self.datetime_of_booking = datetime_of_booking
        self.fullfilled = fullfilled

def view_appointments(request):
    if not request.user.is_authenticated:
        return redirect('user-login')

    appointments : list[Appointment]
    appointments = []

    pending_appointment = None

    if DonorAppointment.objects.filter(user_id=request.user).exists():
        donor_appointments = DonorAppointment.objects.filter(user_id=request.user)
        for donor_appointment in donor_appointments:
            clinic_name = Clinic.objects.get(clinic_id=donor_appointment.clinic_id.clinic_id).name
            appointment = Appointment(
                type='Donor',
                clinic_name=clinic_name,
                datetime_of_appointment=donor_appointment.datetime_of_appointment,
                datetime_of_booking=donor_appointment.datetime_of_booking,
                fullfilled=donor_appointment.appointment_fullfilled
                )
            if not appointment.fullfilled:
                pending_appointment = appointment
            appointments.append(appointment)

    if PatientAppointment.objects.filter(user_id=request.user).exists():
        patient_appointments = PatientAppointment.objects.filter(user_id=request.user)
        for patient_appointment in patient_appointments:
            clinic_name = Clinic.objects.get(id=patient_appointment.clinic_id).name
            appointment = Appointment(
                type='Patient',
                clinic_name=clinic_name,
                datetime_of_appointment=patient_appointment.datetime_of_appointment,
                datetime_of_booking=patient_appointment.datetime_of_booking,
                fullfilled=patient_appointment.appointment_fullfilled
                )
            if not appointment.fullfilled:
                pending_appointment = appointment
            appointments.append(appointment)

    appointments.sort(key=lambda x: x.datetime_of_appointment)
    context = {'appointments': appointments, 'pending_appointment': pending_appointment}
    return render(request, 'base/view-appointments.html', context)


def donations(request):
    context = {}
    return render(request, TEMPLATE_DONATIONS, context)

def volunteer(request):
    context = {}
    return render(request, TEMPLATE_VOLUNTEER, context)


def not_allowed(request):
    context = {}
    return render(request, 'not-allowed.html', context)

