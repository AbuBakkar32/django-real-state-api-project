from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Agent
from .serializers import AgentSerializer


# Create your views here.
class AgentListAPIView(ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None


class AgentDetailAPIView(RetrieveAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class AgentListTopSellerAPIView(ListAPIView):
    queryset = Agent.objects.filter(top_seller=True)
    serializer_class = AgentSerializer
    permission_classes = (permissions.AllowAny,)
