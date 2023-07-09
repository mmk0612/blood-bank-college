from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from users.models import Profile
from django.contrib import messages

# Create your views here.

def staff_homepage(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to view the staff homepage.')
        return redirect('user-login')
    if not request.user.is_staff:
        messages.error(request, 'You must be a staff member to view the staff homepage.')
        return render(request, 'not_allowed.html')

    context = {}
    staff = Staff.objects.get(user_id=request.user)
    blood_available = BloodAvailable.objects.filter(clinic_id=staff.clinic_id)
    context['blood_available'] = blood_available

    return render(request, 'staff/homepage.html', context)


def view_appointments(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to view your appointments.')
        return redirect('user-login')
    if not request.user.is_staff:
        messages.error(request, 'You must be a staff member to view appointments.')
        return render(request, 'not_allowed.html')

    query_name = request.GET.get('name', '')
    staff = Staff.objects.get(user_id=request.user)

    appointments = []
    appointments = Appointment.objects.filter(clinic_id=staff.clinic_id)

    appointments.order_by('datetime_of_appointment')

    context = {'appointments': appointments}
    return render(request, 'staff/view-appointments.html', context)


def fullfill_appointment(request, appointment_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to fullfill an appointment.')
        return redirect('user-login')
    if not request.user.is_staff:
        messages.error(request, 'You must be a staff member to fullfill an appointment.')
        return render(request, 'not-allowed.html')

    appointment_id = int(appointment_id)

    staff = Staff.objects.get(user_id=request.user)

    context = {}

    if Appointment.objects.filter(appointment_id=appointment_id).exists():
        appointment = Appointment.objects.get(appointment_id=appointment_id)
        context['appointment'] = appointment
        if appointment.appointment_fullfilled:
            if appointment.type == 'Donor':
                bloods = BloodFromDonor.objects.filter(appointment_id=appointment)
            else:
                bloods = BloodToPatient.objects.filter(appointment_id=appointment)
            context['bloods'] = bloods
            return render(request, 'staff/already-fullfilled.html', context)
        if request.method == 'POST':
            form = BloodUnitsForm(request.POST)
            if form.is_valid():
                blood_units = form.cleaned_data['units']
                bloods = []
                for i in range(blood_units):
                    if appointment.type == 'Donor':
                        blood = BloodFromDonor(appointment_id = appointment)
                    else:
                        blood = BloodToPatient(appointment_id = appointment)
                    try:
                        blood.full_clean()
                    except ValidationError as e:
                        messages.error(request, 'Error: ' + str(e))
                        return render(request, 'staff/fullfill-appointment.html')
                    bloods.append(blood)
                if appointment.type == 'Donor':
                    BloodFromDonor.objects.bulk_create(bloods)
                else:
                    BloodToPatient.objects.bulk_create(bloods)
                appointment.appointment_fullfilled = True
                appointment.save()
                context['bloods'] = bloods
                messages.success(request, 'Appointment fullfilled successfully.')
                return render(request, 'staff/already-fullfilled.html', context)
        else:
            form = BloodUnitsForm()
        context['form'] = form
        return render(request, 'staff/fullfill-appointment.html', context)


    return render(request, 'does-not-exist.html')

