from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Profile(AbstractUser):
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=3)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()
    date_of_registration = models.DateField(auto_now_add=True)
    weight = models.IntegerField()
    date_of_birth = models.DateField()

