from django import forms
from enum import Enum

from staff.models import Clinic

class CreateAppointmentForm(forms.Form):
    clinic = forms.CharField(
            widget=forms.Select(
                attrs={'class': 'form-control'},
                choices=[(0, "Select a Clinic")] + [(clinic.clinic_id, clinic.name+', '+clinic.state) for clinic in Clinic.objects.all()],
            ),
            initial="Select a clinic",
            required=True,
            error_messages={'required': 'Please select a clinic.'}
        )
    datetime = forms.DateField(
            widget=forms.DateInput(
                attrs={'class': 'form-control'},
            ),
            input_formats = ['%d-%m-%Y'],
            required=True,
            error_messages={'required': 'Please select a date and time.'},
        )
    type = forms.CharField(
            widget = forms.Select(
                attrs={'class': 'form-control'},
                choices=[('', 'Select type of Appointment'), ('Donor', 'Donor'), ('Patient', 'Patient')],
                ),
            required=True,
            error_messages={'required': 'Please select a type.'}
        )

    def clean_clinic(self):
        clinic = self.cleaned_data['clinic']
        if clinic == 'Select a clinic':
            raise forms.ValidationError('Please select a clinic.')
        return clinic



