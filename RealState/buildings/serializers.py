from rest_framework import serializers
from .models import Home, ImageFiles


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = (
        'title', 'slug', 'photo', 'bathrooms', 'bedrooms', 'sqft', 'photo', 'price', 'address', 'city', 'state',
        'zipcode', 'sale_type', 'home_type')


class HomeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
        lookup_field = 'slug'


class ImageFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFiles
        fields = '__all__'
        lookup_field = 'home'
