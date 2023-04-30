from django.shortcuts import render
from rest_framework import status, permissions, generics
from rest_framework.pagination import PageNumberPagination

from .serializers import ContactSerializer
from .models import Contact
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
# API View
class ContactAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def put(self, request, *args, **kwargs):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Modifying the pagination style
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10


# Generic View
class ContactListCreateAPIView(ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    pagination_class = StandardResultsSetPagination


class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = 'id'
