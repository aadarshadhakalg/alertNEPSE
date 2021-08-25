from datetime import datetime
from rest_framework import response
from authentication.models import AccountUser
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChangePasswordSerializer, RegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer

# Create your views here.

class RegisterView(APIView):
    
    def post(self,request:Request,format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data='User created successfully',status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)



class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self,request:Request,format=None,*args,**kwargs):
        serializer = ChangePasswordSerializer(data=request.data)

        if(serializer.is_valid()):
            user : AccountUser = request.user
            if(user.check_password(request.data['old_password'])):
                serializer.update(instance=request.user,validated_data=serializer.validated_data)
                return Response({
                    'message':"Password Changed Successfully"
                },status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)