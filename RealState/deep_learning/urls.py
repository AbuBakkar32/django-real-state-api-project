# import urls.py from deep_learning app

# Path: RealState\deep_learning\urls.py
from django.urls import path
from .views import deep_learning

urlpatterns = [
    path('', deep_learning, name='dl'),

]
