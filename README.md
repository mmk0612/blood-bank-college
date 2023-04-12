
# Blood Bank Website and Database
stupid ass project for a stupid ass student in a stupid ass college

# TODO

- [ ] figure out how to encrypt messages


# ideas

## website

org name , logo , slogan
phone number
nav bar
    home, about us, events, donate blood, merchandise (coming soon), faq

buttons : donate blood, request blood
input box : ??

count of donors connected

strip
    volunteer, money donation, events

importance of blood randi rona

bottom strip
    site map
    about us
    contact us

on the right recent donors going up like my soul leaving my body


## sql

- interface for staff
    can add blood donor
    can remove blood

- blood bank locations

- events

- hospitals

- blood -> hospital

- blood

- money donors

- blood donors


# FUTURE

merchandise

-- pre filled (admin)
CLINICS
    clinic_id, address, pincode, state

BLOOD_AVAILABLE (filled by triggers)
    clinic_id, blood_group, units_available

/login (user and staff)
staff registration is done by admin (pre-filled)
USERS (username)

STAFF_CLINIC
    staff_id, user_id, clinic_id

/register (user)
USER
    username, name, gender, age, phone, blood_group, state, pincode, date_of_reg, weight, date_of_birth
    user_id (auto generated)

after login, they have three options, donate, request and view appointments

    if there is already a pending appointment then dont allow these 2

    /donate
    donate
        show the nearest clinic

    /request
    request
        input units needed
        show various clinics and for each clinic
            show if the blood will be available

  for both options show a form to 
        select date
        file an appointment

    /view-appointments
    view all the appointments (past and pending)

max_appointments_per_day_per_clinic = 5
DONOR_APPOINTMENTS
    donor_appointment_id, user_id, clinic_id, datetime_of_appointment, appointment_fullfilled

PATIENT_APPOINTMENT
    patient_appointment_id, user_id, clinic_id, amount_to_donate, appointment_fullfilled

/staff-homepage
show 4 options

/view-appointment
    if the person has an appointment, mark appointment fullfilled

/create-appointment
    if the person does not have an appointment,
        if request, then check if blood is available and then 
            if yes
                create appointment
            else
                fuck off
        if donation
            create appointment

/donate-blood (staff)
    staff will enter units of blood donated to the clinic and the system will handle the rest
BLOOD table
    blood_id, appointment_id
1 blood_id is 1 unit

/request-blood (staff)
    staff will enter units of blood donated to the patiend and the system will do the rest
DONATED_TO_PATIENT_BLOOD
    blood_id, appointment_id

/view-analytics (staff) (future scope)
    show how much blood available at the clinic and other stats
        other stats like
            how much blood recieved in past x days
            how much blood donated in past x days


