from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2', 'age', 'phone', 'blood_group', 'state', 'pincode', 'weight', 'date_of_birth')

class UserLoginForm(AuthenticationForm):
    pass

