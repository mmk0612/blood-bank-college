from django.core.management.base import BaseCommand
from staff.models import Clinic


class Command(BaseCommand):
    def handle(self, **options):
        clinic_id = input('Clinic_ID: ')
        clinic = Clinic.objects.get(clinic_id = clinic_id) #type: ignore
        if not clinic:
            print('Clinic does not exist')
            return

        clinic.delete()

        print('Clinic deleted')
