from django.http import response
from rest_framework import serializers
from authentication.models import AccountUser
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework import status

# Create your views here.

class RegisterView(APIView):
    
    def post(self,request:Request,format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            instance : AccountUser = serializer.create(serializer.validated_data)
            instance.save()
            return Response(
                {
                    "user": RegistrationSerializer(instance).data
                },
                status= status.HTTP_201_CREATED

            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)

    def get_serializer(self):
        return RegistrationSerializer()