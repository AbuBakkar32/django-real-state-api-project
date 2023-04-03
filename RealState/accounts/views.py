from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework.decorators import api_view


# GithubAthentication - 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

# Create your views here.
@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            data['response'] = "Successfully registered a new user."
            data['email'] = user.email
            data['username'] = user.username
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            token = RefreshToken.for_user(user).access_token
            data['token'] = str(token)
        else:
            data = serializer.errors
        return Response(data)
