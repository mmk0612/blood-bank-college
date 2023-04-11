from django.urls import path
from .views import *

urlpatterns = [

    path('homepage/', staff_homepage, name='staff-homepage'),

]
