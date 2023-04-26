# Generated by Django 4.1.5 on 2023-04-14 21:20

from django.db import migrations

def add_clinic_for_mihir(apps, schema_editor):
    Profile = apps.get_model('users', 'Profile')
    mihir = Profile.objects.get(username='mihir')
    Clinic = apps.get_model('staff', 'Clinic')
    clinic = Clinic.objects.get(clinic_id=10)
    Staff = apps.get_model('staff', 'Staff')
    Staff.objects.create(
        user_id=mihir,
        clinic_id=clinic
            )


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20230414_1917'),
        ('users', '0002_auto_20230414_1923')
    ]

    operations = [
        migrations.RunPython(add_clinic_for_mihir)
    ]
