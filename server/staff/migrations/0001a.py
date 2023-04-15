from django.db import migrations

SQL_QUERIES = """
create trigger bloodavailable_insert after insert on staff_clinic
for each row
    insert into staff_bloodavailable(blood_group, units_available, clinic_id_id) values
        ('A+', 0, new.clinic_id),
        ('A-', 0, new.clinic_id),
        ('B+', 0, new.clinic_id),
        ('B-', 0, new.clinic_id),
        ('AB+', 0, new.clinic_id),
        ('AB-', 0, new.clinic_id),
        ('O+', 0, new.clinic_id),
        ('O-', 0, new.clinic_id);
        ;
create trigger bloodavailable_add after insert on staff_bloodfromdonor
for each row
    update staff_bloodavailable set units_available=units_available+1
    where
        blood_group=(
            select users_profile.blood_group from staff_appointment, users_profile
            where
                staff_appointment.appointment_id = new.appointment_id_id
                and
                users_profile.id = staff_appointment.user_id_id
        )
    ;
create trigger bloodavailable_add after insert on staff_bloodtopatient
for each row
    update staff_bloodavailable set units_available=units_available-1
    where
        blood_group=(
            select users_profile.blood_group from staff_appointment, users_profile
            where
                staff_appointment.appointment_id = new.appointment_id_id
                and
                users_profile.id = staff_appointment.user_id_id
        )
    ;
INSERT INTO staff_clinic VALUES(1,'vsdvsdf',12432,'Bihar','ABCD');
"""

def run_sql(apps, schema_editor):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(SQL_QUERIES)

class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('users', '0005_auto_20230415_1001')
    ]

    operations = [
        migrations.RunPython(run_sql)
    ]
