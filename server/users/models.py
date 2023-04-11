from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class BloodGroupEnum(models.TextChoices):
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    B_POSITIVE = 'B+'
    B_NEGATIVE = 'B-'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'

class StateEnum(models.TextChoices):
    ANDHRA_PRADESH = 'Andhra Pradesh'
    ASSAM = 'Assam'
    BIHAR = 'Bihar'
    CHANDIGARH = 'Chandigarh'
    CHATTISGARH = 'Chattisgarh'
    DELHI = 'Delhi'
    GOA = 'Goa'
    GUJARAT = 'Gujarat'
    HARYANA = 'Haryana'
    HIMACHAL_PRADESH = 'Himachal Pradesh'
    JAMMU_AND_KASHMIR = 'Jammu and Kashmir'
    JHARKHAND = 'Jharkhand'
    KARNATAKA = 'Karnataka'
    KERALA = 'Kerala'
    MADHYA_PRADESH = 'Madhya Pradesh'
    MAHARASHTRA = 'Maharashtra'
    MEGHALAYA = 'Meghalaya'
    MIZORAM = 'Mizoram'
    ODISHA = 'Odisha'
    PUNJAB = 'Punjab'
    RAJASTHAN = 'Rajasthan'
    TAMIL_NADU = 'Tamil Nadu'
    UTTARAKHAND = 'Uttarakhand'
    UTTAR_PRADESH = 'Uttar Pradesh'
    WEST_BENGAL = 'West Bengal'


class Profile(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=3, choices=BloodGroupEnum.choices)
    state = models.CharField(max_length=20, choices=StateEnum.choices)
    city = models.CharField(max_length=20)
    pincode = models.IntegerField()
    date_of_registration = models.DateField(auto_now_add=True)
    weight = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField()

