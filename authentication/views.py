from django.http import response
from rest_framework import serializers
from authentication.models import User
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework import permissions

# Create your views here.

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    
    def post(self,request:Request,format=None):
        serializer = UserSerializer()
        instance : User = serializer.create(request.data)

        password = request.data['password']

        instance.set_password(password)
        instance.save()
        return Response(
            {
                "user": UserSerializer(instance).data
            },
            status= status.HTTP_201_CREATED

        )

    def get_serializer(self):
        return UserSerializer()