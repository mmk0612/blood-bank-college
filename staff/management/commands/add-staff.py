from django.core.management.base import BaseCommand
from staff.models import Staff, Clinic
from users.models import Profile


class Command(BaseCommand):
    def handle(self, **options):
        username = input('Username: ')
        user = Profile.objects.get(username = username)
        if not user:
            print('User does not exist')
            return
        if user.is_staff:
            print('User is already a staff')
            return

        clinic_id = input('Clinic_ID: ')
        clinic = Clinic.objects.get(id = clinic_id) # type: ignore
        if not clinic:
            print('Clinic does not exist')
            return
        staff = Staff(
                user_id = user,
                clinic_id = clinic.id,
                )
        user.is_staff = True
        staff.save()
        user.save()

        print('Staff added')
