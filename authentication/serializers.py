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
        validated_data.pop('password_verify')
        return super().create(validated_data)


    def update(self, instance, validated_data):
        return super().update(instance, validated_data)



class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    new_password_verify = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] == attrs['old_password']:
            raise serializers.ValidationError('New password can not be same as old password.')
        if attrs['new_password'] == attrs['new_password_verify']:
            raise serializers.ValidationError('New Password and Verify Password field did not match.')
        return super().validate(attrs)
