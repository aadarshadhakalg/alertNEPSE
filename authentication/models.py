from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone: CharField(unique=True,max_length=13,null=False)
    verified: BooleanField(default=False,null=False)
    is_superuser: BooleanField(default=False,null=False)
    is_staff: BooleanField(default=False,null=False)


