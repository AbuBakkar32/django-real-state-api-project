from django.urls import path, include
from .views import ContactAPIView, ContactListCreateAPIView, ContactRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('', ContactAPIView.as_view(), name="register"),
    path('list/', ContactListCreateAPIView.as_view(), name="list"),
    path('list/<int:id>/', ContactRetrieveUpdateDestroyAPIView.as_view(), name="list"),
]
