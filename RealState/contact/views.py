from django.shortcuts import render
from rest_framework import status, permissions, generics
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
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
