from rest_framework import serializers
from .models import AccountUser

class RegistrationSerializer(serializers.ModelSerializer):    

    password_verify = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password_verify']:
            raise serializers.ValidationError('Password did not match')
        return super().validate(attrs)

    class Meta:
        model = AccountUser
        exclude = ['is_staff','last_login','date_joined','verified','is_superuser','is_active']
        


    def create(self, validated_data) -> AccountUser:
        user : AccountUser = AccountUser.objects.create(
        phone = validated_data.get('phone'),
        first_name = validated_data.get('first_name'),
        last_name = validated_data.get('last_name'),
        email = validated_data.get('email'))
        user.set_password(validated_data.get('password'))

        user.save()
        return user



class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    new_password_verify = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] == attrs['old_password']:
            raise serializers.ValidationError('New password can not be same as old password.')
        if attrs['new_password'] != attrs['new_password_verify']:
            raise serializers.ValidationError('New Password and Verify Password field did not match.')
        return super().validate(attrs)


    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()

        return instance
