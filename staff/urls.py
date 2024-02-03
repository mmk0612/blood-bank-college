from django.urls import path
from .views import *

urlpatterns = [

    path('homepage/', staff_homepage, name='staff-homepage'),
    path('view-appointments/', view_appointments, name='staff-view-appointments'),
    path('view-appointments/<int:appointment_id>/', fullfill_appointment, name='staff-fullfill-appointment'),

]
