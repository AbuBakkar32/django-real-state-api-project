# import urls.py from data_analysis app

# Path: RealState\data_analysis\urls.py
from django.urls import path
from .views import data_analysis

urlpatterns = [
    path('', data_analysis, name='da'),

]
