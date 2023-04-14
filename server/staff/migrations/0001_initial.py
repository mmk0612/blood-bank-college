# Generated by Django 4.1.5 on 2023-04-14 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Donor', 'Donor'), ('Patient', 'Patient')], max_length=10)),
                ('datetime_of_appointment', models.DateTimeField()),
                ('datetime_of_booking', models.DateTimeField(auto_now_add=True)),
                ('appointment_fullfilled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('clinic_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chattisgarh', 'Chattisgarh'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu And Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Tamil Nadu', 'Tamil Nadu'), ('Uttarakhand', 'Uttarakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('clinic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.clinic')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BloodToPatient',
            fields=[
                ('blood_id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='BloodFromDonor',
            fields=[
                ('blood_id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='BloodAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('A+', 'A Positive'), ('A-', 'A Negative'), ('B+', 'B Positive'), ('B-', 'B Negative'), ('AB+', 'Ab Positive'), ('AB-', 'Ab Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')], max_length=3)),
                ('units_available', models.IntegerField()),
                ('clinic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.clinic')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='clinic_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.clinic'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
