# import urls.py from machine_learning app

# Path: RealState\machine_learning\urls.py
from django.urls import path
from .views import machine_learning

urlpatterns = [
    path('', machine_learning, name='ml'),

]
