# import urls.py from Blogs app

# Path: RealState\Blogs\urls.py
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),

]