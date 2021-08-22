from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        exclude = ['is_staff','groups','user_permissions','is_superuser']


    def create(self, validated_data) -> User:
        return super().create(validated_data)


    def update(self, instance, validated_data):
        return super().update(instance, validated_data)