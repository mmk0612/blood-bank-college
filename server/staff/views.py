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


def view_appointments(request):
    if not request.user.is_authenticated:
        return redirect('user-login')
    if not request.user.is_staff:
        return render(request, 'not_allowed.html')

    query_name = request.GET.get('name', '')
    staff = Staff.objects.get(user_id=request.user)

    appointments = []
    appointments = Appointment.objects.filter(clinic_id=staff.clinic_id)

    appoinments.sort(key=lambda x: x.datetime_of_appointment)

    context = {'appointments': appointments}
    return render(request, 'staff/view-appointments.html', context)


def fullfill_appointment(request, appointment_id):
    if not request.user.is_authenticated:
        return redirect('user-login')
    if not request.user.is_staff:
        return render(request, 'not-allowed.html')

    staff = Staff.objects.get(user_id=request.user)

    if Appointment.objects.filter(appointment_id=appointment_id).exists():
        appointment = Appointment.objects.get(appointment_id=appointment_id)
        context = {'appointment': appointment}
        if appointment.appointment_fullfilled:
            return render(request, 'staff/already-fullfilled.html')
        if request.method == 'POST':
            form = BloodUnitsForm(request.POST)
            if form.is_valid():
                blood_units = form.cleaned_data['blood_units']
                bloods = []
                for i in range(blood_units):
                    if appointment.appointment_type == 'Donor':
                        blood = BloodFromDonor(appointment_id = appointment)
                    else:
                        blood = BloodToPatient(appointment_id = appointment)
                    try:
                        blood.full_clean()
                    except ValidationError as e:
                        return render(request, 'staff/fullfill-appointment.html', {'errors': e})
                    bloods.append(blood)
                if appointment.appointment_type == 'Donor':
                    BloodFromDonor.objects.bulk_create(bloods)
                else:
                    BloodToPatient.objects.bulk_create(bloods)
                appointment.appointment_fullfilled = True
                appointment.save()
                return render(request, 'staff/already-fullfilled.html', context)
            else:
                return render(request, 'staff/fullfill-appointment.html', {'form': form})

    return render(request, 'does-not-exist.html')

