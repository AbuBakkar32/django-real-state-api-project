from django.urls import path, include
from .views import AgentListAPIView, AgentDetailAPIView, AgentListTopSellerAPIView
urlpatterns = [
    path('', AgentListAPIView.as_view(), name="list"),
    path('<pk>', AgentDetailAPIView.as_view(), name="details"),
    path('topseller', AgentListTopSellerAPIView.as_view(), name="top-seller"),
]
