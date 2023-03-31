from django.shortcuts import render
from .forms import RequestBloodForm
from .db import cursor
from django.http import HttpResponse

# Create your views here.

def test(request):
    if request.method == 'POST':
        form = RequestBloodForm(request.POST)
        print(form)
        # if form.is_valid():
            # print(form.cleaned_data)
            # patient_name = form.cleaned_data['patient_name']
            # doctor_name = form.cleaned_data['doctor_name']
            # blood_group = form.cleaned_data['blood_group']
            # hospital_name_address = form.cleaned_data['hospital_name_address']
            # cursor.execute("INSERT INTO request_blood (patient_name, doctor_name, blood_group, hospital_name_address) VALUES (?, ?, ?, ?)", (patient_name, doctor_name, blood_group, hospital_name_address))
        return HttpResponse("Success")

    return HttpResponse("Failure")



