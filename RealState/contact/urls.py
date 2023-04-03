from django.urls import path, include
from .views import ContactAPIView
urlpatterns = [
    path('', ContactAPIView.as_view(), name="register"),
]
