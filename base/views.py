from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from staff.models import Clinic, Appointment, BloodFromDonor, MoneyReceived
from .forms import CreateAppointmentForm

# Create your views here.
def homepage(request):
    context = {}
    return render(request, "base/homepage.html", context)

def events(request):
    context = {}
    return render(request, "base/events.html", context)

def about_us(request):
    context = {}
    return render(request, "base/about-us.html", context)


def create_appointment(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to create an appointment.')
        return redirect('user-login')

    # find if already an appointment
    context = {}

    if Appointment.objects.filter(user_id=request.user, appointment_fullfilled=False).exists():
        messages.error(request, 'You already have an appointment.')
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
        messages.error(request, 'You must be logged in to view your appointments.')
        return redirect('user-login')

    appointments = Appointment.objects.filter(user_id=request.user)
    pending_appointment = None
    if Appointment.objects.filter(user_id=request.user, appointment_fullfilled=False).exists():
        pending_appointment = Appointment.objects.get(user_id=request.user, appointment_fullfilled=False)

    appointments.order_by('datetime_of_appointment')
    context = {'appointments': appointments, 'pending_appointment': pending_appointment}
    return render(request, 'base/view-appointments.html', context)


def donations(request):
    donors = MoneyReceived.objects.all()
    context = {'donors': donors}
    return render(request, "base/donations.html", context)

def not_allowed(request):
    context = {}
    return render(request, 'not-allowed.html', context)


class RecentDonors:
    def __init__(self, name, state, blood_donated, datetime_of_appointment):
        self.name = name
        self.state = state
        self.blood_donated = blood_donated
        self.datetime_of_appointment = datetime_of_appointment

def recent_donors(request):
    "Show last 10 blood donors"

    context = {}

    appointments = Appointment.objects.all().filter(appointment_fullfilled=True).order_by('-datetime_of_appointment')[:10]
    recent_donors = []

    for appointment in appointments:
        name = appointment.user_id.first_name + " " + appointment.user_id.last_name
        state = appointment.user_id.state
        blood_donated = len(BloodFromDonor.objects.all().filter(appointment_id=appointment))
        datetime_of_appointment = appointment.datetime_of_appointment
        recent_donors.append(RecentDonors(name, state, blood_donated, datetime_of_appointment))

    context['recent_donors'] = recent_donors

    return render(request, 'base/recent-donors.html', context)

