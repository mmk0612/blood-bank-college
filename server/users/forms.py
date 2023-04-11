from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import Profile, StateEnum, BloodGroupEnum

class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2', 'phone', 'blood_group', 'state', 'pincode', 'weight', 'date_of_birth', 'city')


    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    blood_group = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=BloodGroupEnum.choices))
    state = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=StateEnum.choices))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pincode = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    weight = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class ProfileLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

