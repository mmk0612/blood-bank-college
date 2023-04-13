from django import forms


class BloodUnitsForm(forms.Form):
    # units have to be more than 0 and less than 3
    units = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), min_value=1, max_value=3)


