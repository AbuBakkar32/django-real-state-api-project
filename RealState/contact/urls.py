from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ContactAPIView, ContactListCreateAPIView, ContactRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('', ContactAPIView.as_view(), name="api_view"),
    path('list/', ContactListCreateAPIView.as_view(), name="list"),
    path('list/<int:id>/', ContactRetrieveUpdateDestroyAPIView.as_view(), name="list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)