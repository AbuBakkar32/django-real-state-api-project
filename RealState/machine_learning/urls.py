# import urls.py from machine_learning app

# Path: RealState\machine_learning\urls.py
from django.urls import path
from .views import machine_learning, registration

urlpatterns = [
    path('', machine_learning, name='ml'),
    path('registration/', registration, name='registration'),

]
