from authentication.models import AccountUser
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChangePasswordSerializer, RegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.

class RegisterView(APIView):
    
    def post(self,request:Request,format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "user": serializer.data
                },
                status= status.HTTP_201_CREATED

            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)

    def get_serializer(self):
        return RegistrationSerializer()



class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self,request:Request,format=None,*args,**kwargs):
        serializer = ChangePasswordSerializer(data=request.data)

        if(serializer.is_valid()):
            user : AccountUser = request.user
            if(user.check_password(request.data['old_password'])):
                instance : AccountUser = serializer.update(request.user,serializer.validated_data)
                instance.set_password(request.data['new_password'])
                instance.save()
                return Response({
                    'message':"Password Changed Successfully"
                },status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)