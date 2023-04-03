from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Home, ImageFiles
from .serializers import HomeSerializer, HomeDetailsSerializer, ImageFilesSerializer
from rest_framework.views import APIView


# Create your views here.
class HomeListAPIView(ListAPIView):
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    serializer_class = HomeSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'


class HomeDetailsAPIView(RetrieveAPIView):
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    serializer_class = HomeDetailsSerializer
    lookup_field = 'slug'


class ImageView(APIView):
    def get(self, request, pk, format=None):
        home = Home.objects.get(pk=pk)
        images = home.images.all()
        serializer = ImageFilesSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
