from rest_framework import serializers
from .models import AccountUser

class RegistrationSerializer(serializers.ModelSerializer):    

    password_verify = serializers.CharField()

    def validate(self, attrs):
        if attrs['password'] != attrs['password_verify']:
            raise serializers.ValidationError('Password did not match')
        return super().validate(attrs)

    class Meta:
        model = AccountUser
        # fields = ['verified','phone','password_verify']
        exclude = ['is_staff','last_login','date_joined','verified','is_superuser','is_active']
        


    def create(self, validated_data) -> AccountUser:
        return super().create(validated_data)


    def update(self, instance, validated_data):
        return super().update(instance, validated_data)



class SignInSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountUser
        fields = ['email','password']