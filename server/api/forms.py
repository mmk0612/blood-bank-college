from django import forms

class RequestBloodForm(forms.Form):
    patient_name = forms.CharField(max_length=100)
    doctor_name = forms.CharField(max_length=100)
    blood_group = forms.CharField(max_length=3)
    hospital_name_address = forms.CharField(max_length=200)


