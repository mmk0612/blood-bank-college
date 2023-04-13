from django.core.management.base import BaseCommand
from staff.models import Clinic


class Command(BaseCommand):
    def handle(self, **options):
        address = input('Address: ')
        pincode = input('Pincode: ')
        state = input('State: ')

        clinic = Clinic(
                address = address,
                pincode = pincode,
                state = state,
                )
        if clinic.full_clean():
            print('Clinic is valid')
        else:
            print('Clinic is invalid')
            return
        clinic.save()

        print(f'Clinic added : {clinic}')
