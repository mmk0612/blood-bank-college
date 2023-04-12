from django.urls import path
from .views import *

urlpatterns = [

    path('', homepage, name='homepage'),
    path('events/', events, name='events'),
    path('about-us/', about_us, name='about-us'),
    path('donate-blood/', donate_blood, name='donate-blood'),
    path('request-blood/', request_blood, name='request-blood'),
    path('donations/', donations, name='donations'),
    path('volunteer/', volunteer, name='volunteer'),

        ]
