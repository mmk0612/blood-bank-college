from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from staff.models import Clinic, Appointment
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

    if Appointment.objects.filter(user_id=request.user).exists():
        return render(request, 'base/already-appointment.html', context)

    if request.method == 'POST':
        form = CreateAppointmentForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            clinic_id = form.cleaned_data['clinic']
            clinic = Clinic.objects.get(clinic_id=clinic_id)
            datetime_of_appointment = form.cleaned_data['datetime']
            appointment = Appointment(user_id=request.user, type=type, clinic_id=clinic, datetime_of_appointment=datetime_of_appointment)

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

def view_appointments(request):
    if not request.user.is_authenticated:
        return redirect('user-login')

    appointments = Appointment.objects.filter(user_id=request.user)
    pending_appointment = None
    if Appointment.objects.filter(user_id=request.user, appointment_fullfilled=False).exists():
        pending_appointment = Appointment.objects.get(user_id=request.user, appointment_fullfilled=False)

    appointments.order_by('datetime_of_appointment')
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

