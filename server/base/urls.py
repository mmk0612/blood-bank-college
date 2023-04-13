from django.urls import path
from .views import *

urlpatterns = [

    path('', homepage, name='homepage'),
    path('events/', events, name='events'),
    path('about-us/', about_us, name='about-us'),
    path('create-appointment/', create_appointment, name='user-create-appointment'),
    path('view-appointments/', view_appointments, name='user-view-appointments'),
    path('donations/', donations, name='donations'),

        ]
