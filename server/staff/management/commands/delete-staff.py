from django.core.management.base import BaseCommand
from staff.models import Staff
from users.models import Profile


class Command(BaseCommand):
    def handle(self, **options):
        username = input('Username: ')
        user = Profile.objects.get(username = username)
        if not user:
            print('User does not exist')
            return
        if not user.is_staff:
            print('User is not a staff')
            return

        staff = Staff.objects.get(user_id = user)
        if not staff:
            print('Staff does not exist')
            return

        staff.delete()
        user.is_staff = False
        user.save()

        print('Staff deleted')
