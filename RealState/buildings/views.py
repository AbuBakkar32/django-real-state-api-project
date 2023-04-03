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


class Search(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        queryset_list = Home.objects.all()
        # City
        if 'city' in request.data:
            city = request.data['city']
            if city:
                queryset_list = queryset_list.filter(city__icontains=city)

        # State
        if 'state' in request.data:
            state = request.data['state']
            if state:
                queryset_list = queryset_list.filter(state__icontains=state)

        # Bedrooms
        if 'bedrooms' in request.data:
            bedrooms = request.data['bedrooms']
            if bedrooms:
                queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

        serializer = HomeSerializer(queryset_list, many=True)
        return Response(serializer.data)
